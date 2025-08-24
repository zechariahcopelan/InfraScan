#!/usr/bin/env python3
"""
InfraScan CLI - Command line system monitoring tool
Usage: python cli.py [options]
"""

import argparse
import csv
from datetime import datetime
from system_monitor import get_all_metrics, get_cpu_usage, get_memory_usage, get_disk_usage, get_network_latency, get_process_info


def print_cpu(data):
    """Display CPU information"""
    print("💻 CPU Usage")
    print(f"   Usage: {data['cpu_percent']}%")
    print(f"   Cores: {data['cpu_count']}")
    print()


def print_memory(data):
    """Display memory information"""
    print("🧠 Memory Usage")
    print(f"   Used: {data['used_gb']}GB / {data['total_gb']}GB ({data['percent']}%)")
    print(f"   Available: {data['available_gb']}GB")
    print()


def print_disk(data):
    """Display disk information"""
    print("💾 Disk Usage")
    print(f"   Used: {data['used_gb']}GB / {data['total_gb']}GB ({data['percent']}%)")
    print(f"   Free: {data['free_gb']}GB")
    print()


def print_network(data):
    """Display network information"""
    print("🌐 Network")
    if data['latency_ms']:
        status_icon = "✅" if data['latency_ms'] < 50 else "⚠️" if data['latency_ms'] < 100 else "❌"
        print(f"   Latency: {data['latency_ms']}ms {status_icon}")
    else:
        print("   Latency: Failed ❌")
    print(f"   Status: {data['status']}")
    print()


def print_processes(data):
    """Display process information"""
    print("⚡ Processes")
    print(f"   Total: {data['total_processes']}")
    print(f"   Active: {data['active_processes']}")
    
    if data['top_memory']:
        print("   Top Memory Consumers:")
        for i, proc in enumerate(data['top_memory'][:3], 1):
            print(f"     {i}. {proc['name']}: {proc['memory_percent']}%")
    
    if data['top_cpu']:
        print("   Top CPU Consumers:")
        for i, proc in enumerate(data['top_cpu'][:3], 1):
            print(f"     {i}. {proc['name']}: {proc['cpu_percent']}%")
    print()


def export_to_csv(metrics, filename):
    """Export metrics to CSV file"""
    # Flatten the data for CSV
    flat_data = {
        'timestamp': metrics['timestamp'],
        'cpu_percent': metrics['cpu']['cpu_percent'],
        'cpu_count': metrics['cpu']['cpu_count'],
        'memory_total_gb': metrics['memory']['total_gb'],
        'memory_used_gb': metrics['memory']['used_gb'],
        'memory_available_gb': metrics['memory']['available_gb'],
        'memory_percent': metrics['memory']['percent'],
        'disk_total_gb': metrics['disk']['total_gb'],
        'disk_used_gb': metrics['disk']['used_gb'],
        'disk_free_gb': metrics['disk']['free_gb'],
        'disk_percent': metrics['disk']['percent'],
        'network_latency_ms': metrics['network']['latency_ms'],
        'network_status': metrics['network']['status'],
        'total_processes': metrics['processes']['total_processes'],
        'active_processes': metrics['processes']['active_processes'],
        'top_cpu_process': metrics['processes']['top_cpu'][0]['name'] if metrics['processes']['top_cpu'] else '',
        'top_cpu_percent': metrics['processes']['top_cpu'][0]['cpu_percent'] if metrics['processes']['top_cpu'] else 0,
        'top_memory_process': metrics['processes']['top_memory'][0]['name'] if metrics['processes']['top_memory'] else '',
        'top_memory_percent': metrics['processes']['top_memory'][0]['memory_percent'] if metrics['processes']['top_memory'] else 0
    }
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=flat_data.keys())
        writer.writeheader()
        writer.writerow(flat_data)
    
    print(f"📊 Metrics exported to: {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="InfraScan - System monitoring CLI tool",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Metric selection options
    parser.add_argument('--cpu', action='store_true', help='Show CPU usage only')
    parser.add_argument('--memory', action='store_true', help='Show memory usage only')
    parser.add_argument('--disk', action='store_true', help='Show disk usage only')
    parser.add_argument('--network', action='store_true', help='Show network status only')
    parser.add_argument('--processes', action='store_true', help='Show process information only')
    parser.add_argument('--all', action='store_true', help='Show all metrics (default)')
    
    # Export options
    parser.add_argument('--export-csv', metavar='FILENAME', 
                       help='Export metrics to CSV file')
    
    args = parser.parse_args()
    
    # Header
    print("🖥️  InfraScan - System Health Check")
    print("=" * 40)
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Determine what to show
    show_specific = any([args.cpu, args.memory, args.disk, args.network, args.processes])
    show_all = args.all or not show_specific
    
    # Get metrics
    try:
        if show_all:
            metrics = get_all_metrics()
            print_cpu(metrics['cpu'])
            print_memory(metrics['memory'])
            print_disk(metrics['disk'])
            print_network(metrics['network'])
            print_processes(metrics['processes'])
        else:
            if args.cpu:
                cpu_data = get_cpu_usage()
                print_cpu(cpu_data)
            
            if args.memory:
                memory_data = get_memory_usage()
                print_memory(memory_data)
            
            if args.disk:
                disk_data = get_disk_usage()
                print_disk(disk_data)
            
            if args.network:
                network_data = get_network_latency()
                print_network(network_data)
            
            if args.processes:
                process_data = get_process_info()
                print_processes(process_data)
    
    except Exception as e:
        print(f"❌ Error collecting metrics: {e}")
        return 1
    
    # Export to CSV if requested
    if args.export_csv:
        try:
            if 'metrics' not in locals():
                metrics = get_all_metrics()
            export_to_csv(metrics, args.export_csv)
        except Exception as e:
            print(f"❌ Error exporting CSV: {e}")
            return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
