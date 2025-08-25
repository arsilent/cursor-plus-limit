# Claude 3.7 Hack Tool

A simple script to enhance Claude 3.7 in Cursor by:

1. **Increasing token limit** to 200,000 tokens
2. **Setting thinking level** to "high" for more detailed reasoning
3. **Adding custom UI styling** to distinguish the enhanced model

## How It Works

The script uses precise string matching to find and modify specific functions:

- **Token limit**: Uses multiple patterns and fallbacks to find `getEffectiveTokenLimit` function
- **Thinking level**: Searches for `getModeThinkingLevel(e)`
- **UI styling**: Searches for `_serializableTitle:()=>"claude-3.7-sonnet"}`

This approach provides reliable matches across different Cursor versions, even when the code has been minified or slightly modified.

## Usage

### Basic Usage

```bash
python hack_claude.py
```

The script automatically finds Cursor's workbench file and applies the modifications.

### Options

```bash
python hack_claude.py --token-mode all_models --ui-style red
```

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--file`, `-f` | file path | (auto-detect) | Path to workbench.desktop.main.js |
| `--token-mode`, `-t` | `claude37_only`, `all_models` | `claude37_only` | Apply token limit to which models |
| `--ui-style`, `-u` | `gradient`, `red`, `animated` | `gradient` | UI style for the hacked model |
| `--skip-backup`, `-s` | flag | False | Skip backup creation |

## Examples

Modify only Claude 3.7 with animated styling:
```bash
python hack_claude.py --ui-style animated
```

Apply the 200K limit to all models:
```bash
python hack_claude.py --token-mode all_models
```

## Notes

- Creates backups before making changes
- Changes are lost when Cursor updates
- Client-side changes only - actual behavior still depends on Anthropic's API
- If you encounter issues, try using a backup file with `--file path/to/backup.js`
