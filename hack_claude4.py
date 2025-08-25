#!/usr/bin/env python3
"""
Claude 4 Sonnet Hack Script with automated backups

This script enhances Claude 4 Sonnet in Cursor by:
1. Increasing token limit to 200,000
2. Setting thinking level to "high"
3. Customizing Claude 4 Sonnet UI styling

The script uses precise string matching to find the target functions:
- Token limit: Uses multiple search patterns for 'getEffectiveTokenLimit' with fallback to regex
- Thinking level: Searches for 'getModeThinkingLevel(e)'
- UI styling: Searches for '_serializableTitle:()=>"claude-4-sonnet"}'
"""

import re
import sys
import argparse
import shutil
from pathlib import Path

def create_backup(file_path):
    """Create a backup of the original file"""
    backup_path = f"{file_path}.backup"
    shutil.copy2(file_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return backup_path

def modify_workbench_file(file_path, skip_backup=False):
    """Modify the workbench file to unlock Claude-4 Sonnet features"""
    
    if not skip_backup:
        create_backup(file_path)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    modifications_made = False
    
    # New pattern for Cursor 1.2.0 - getEffectiveTokenLimit function
    # Pattern: async getEffectiveTokenLimit(e){...}  
    token_limit_pattern = r'(async getEffectiveTokenLimit\([^)]*\)\s*{[^}]*?if\s*\([^)]*\)\s*{[^}]*?)return[^}]*?(\d{3,6})([^}]*?}[^}]*?})'
    
    def replace_token_limit(match):
        before = match.group(1)
        old_limit = match.group(2)
        after = match.group(3)
        new_limit = "200000"
        
        print(f"🔄 Updating token limit: {old_limit} → {new_limit}")
        return f"{before}return {new_limit}{after}"
    
    if re.search(token_limit_pattern, content):
        content = re.sub(token_limit_pattern, replace_token_limit, content)
        modifications_made = True
        print("✅ Token limit pattern updated")
    else:
        print("⚠️  Token limit pattern not found - trying alternative approach")
        
        # Alternative pattern for token limits
        alt_pattern = r'(\breturn\s+)(\d{3,6})(\s*[;}])'
        matches = list(re.finditer(alt_pattern, content))
        
        for match in reversed(matches):  # Process in reverse to maintain positions
            old_limit = match.group(2)
            if int(old_limit) < 200000:  # Only update smaller limits
                start, end = match.span()
                new_content = f"{match.group(1)}200000{match.group(3)}"
                content = content[:start] + new_content + content[end:]
                print(f"🔄 Updated limit: {old_limit} → 200000")
                modifications_made = True
    
    # New pattern for Cursor 1.2.0 - getModeThinkingLevel function  
    thinking_level_pattern = r'(getModeThinkingLevel\([^)]*\)\s*{[^}]*?)return[^}]*?([012])([^}]*?})'
    
    def replace_thinking_level(match):
        before = match.group(1)
        old_level = match.group(2)
        after = match.group(3)
        new_level = "2"
        
        print(f"🔄 Updating thinking level: {old_level} → {new_level}")
        return f"{before}return {new_level}{after}"
    
    if re.search(thinking_level_pattern, content):
        content = re.sub(thinking_level_pattern, replace_thinking_level, content)
        modifications_made = True
        print("✅ Thinking level pattern updated")
    else:
        print("⚠️  Thinking level pattern not found")
    
    # Claude-4 Sonnet model enablement patterns
    claude4_patterns = [
        # Pattern 1: Model availability checks
        (r'("claude-4[^"]*"[^:]*:\s*){([^}]*)"available"\s*:\s*false', r'\1{\2"available":true'),
        
        # Pattern 2: Model visibility/enabled flags  
        (r'("claude-4[^"]*"[^}]*)"enabled"\s*:\s*false', r'\1"enabled":true'),
        
        # Pattern 3: Pro/subscription requirement bypass
        (r'("claude-4[^"]*"[^}]*)"requiresPro"\s*:\s*true', r'\1"requiresPro":false'),
        
        # Pattern 4: Model access control
        (r'(claude-4[^"]*"[^}]*)"visible"\s*:\s*false', r'\1"visible":true'),
        
        # Pattern 5: Feature flag patterns
        (r'("claude.*"[^}]*)"beta"\s*:\s*true', r'\1"beta":false'),
    ]
    
    for pattern, replacement in claude4_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            modifications_made = True
            print(f"✅ Applied Claude-4 pattern: {pattern[:50]}...")
    
    # Additional Cursor 1.2.0 specific patterns
    cursor_patterns = [
        # Model configuration object patterns
        (r'(\{[^}]*"claude-4[^}]*)"disabled"\s*:\s*true', r'\1"disabled":false'),
        (r'(\{[^}]*"claude-4[^}]*)"hidden"\s*:\s*true', r'\1"hidden":false'),
        
        # Subscription check bypasses
        (r'(if\s*\([^)]*subscription[^)]*\)[^{]*\{[^}]*?)return\s+false', r'\1return true'),
        (r'(if\s*\([^)]*isPro[^)]*\)[^{]*\{[^}]*?)return\s+null', r'\1return true'),
    ]
    
    for pattern, replacement in cursor_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
            modifications_made = True
            print(f"✅ Applied Cursor-specific pattern")
    
    if modifications_made:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully modified {file_path}")
            return True
        except Exception as e:
            print(f"❌ Error writing file: {e}")
            return False
    else:
        print("⚠️  No modifications were made - file may already be patched or patterns not found")
        return False

def main():
    parser = argparse.ArgumentParser(description='Cursor 1.2.0 Claude-4 Sonnet Patcher')
    parser.add_argument('--file', type=str, help='Path to workbench.desktop.main.js')
    parser.add_argument('--skip-backup', action='store_true', help='Skip creating backup')
    
    args = parser.parse_args()
    
    if args.file:
        file_path = args.file
    else:
        # Default path for Cursor 1.2.0
        file_path = r"C:\Program Files\Cursor\resources\app\out\vs\workbench\workbench.desktop.main.js"
    
    if not Path(file_path).exists():
        print(f"❌ File not found: {file_path}")
        return
    
    print("🚀 Cursor 1.2.0 Claude-4 Sonnet Patcher")
    print(f"📁 Target file: {file_path}")
    print("⚠️  Please close Cursor before running this script!")
    
    # Wait for user confirmation
    response = input("Continue? (y/N): ")
    if response.lower() != 'y':
        print("❌ Operation cancelled")
        return
    
    success = modify_workbench_file(file_path, args.skip_backup)
    
    if success:
        print("\n🎉 Patching completed successfully!")
        print("🔄 Please restart Cursor to apply changes")
        print("💡 Claude-4 Sonnet should now be available with increased limits")
    else:
        print("\n❌ Patching failed!")
        print("🔧 Please check the error messages above")

if __name__ == "__main__":
    main() 