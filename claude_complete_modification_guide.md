# Comprehensive Guide to Claude 3.7 Customization in Cursor

This document provides detailed instructions for modifying and optimizing various aspects of Claude 3.7 in Cursor, including token limits, thinking level, and UI styling. These modifications are purely client-side and do not require changes to the Anthropic API.

## 1. Increase Claude's Token Context Window

### Technical Background
Claude's token context window is controlled by the `getEffectiveTokenLimit` function. By default, standard Claude models use a 30,000 token limit, while the Max variants use a 200,000 token limit.

### Steps to Increase Context Window

#### Step 1: Locate the `getEffectiveTokenLimit` Function
In the `workbench.desktop.main.js` file (usually at `/resources/app/out/vs/workbench/workbench.desktop.main.js`), search for:
```js
async getEffectiveTokenLimit(e) {
```

#### Step 2: Modify the Function to Use Higher Limits
Replace the original function with this modified version to set a 200,000 token limit:

```js
async getEffectiveTokenLimit(e) {
  if(e.modelName && e.modelName.includes('claude-3.7')) return 200000;
  
  // Original function code below
  const n = e.modelName;
  if (!n) return 3e4;
  const r = `${n}_token_limit`;
  
  // Rest of the original function...
}
```

For all models (not just Claude 3.7):
```js
async getEffectiveTokenLimit(e) {
  return 200000; // Always use 200K limit for all models
  
  // Original function code will never run
  const n = e.modelName;
  // ...
}
```

## 2. Always Set Claude's Thinking Level to High

### Technical Background
Claude's thinking level controls how much reasoning it shows during generation. The "high" level provides the most detailed thinking process.

### Steps to Set Thinking Level to High

#### Step 1: Locate the `getModeThinkingLevel` Function
In the `workbench.desktop.main.js` file, search for:
```js
getModeThinkingLevel(e) {
  return this.getAllModes().find((n) => n.id === e)?.thinkingLevel ?? "none";
}
```

#### Step 2: Modify the Function to Always Return "high"
Replace it with:
```js
getModeThinkingLevel(e) {
  return "high";
}
```

#### Step 3: Verify the `getThinkingLevel` Function
Make sure this function correctly maps "high" to the appropriate enum value. It should look like:
```js
getThinkingLevel(e) {
  switch (e) {
    case "high":
      return tH.HIGH;
    case "medium":
      return tH.MEDIUM;
    default:
      return tH.UNSPECIFIED;
  }
}
```

## 3. Customize Claude 3.7 UI Styling (Rename & Restyle)

### Technical Background
The UI display of Claude models is controlled by style objects that define how models appear in dropdowns and the chat interface.

### Steps to Customize Claude 3.7 Regular (Non-Max)

#### Step 1: Locate the Claude 3.7 UI Definition
Find where the regular Claude 3.7 model is styled by searching for:
```js
a = { ...e, title: "claude-3.7-sonnet", id: r, _serializableTitle: () => "claude-3.7-sonnet" },
```

#### Step 2: Modify the UI Component
Replace with this code to add custom styling:
```js
a = { ...e, title: "claude-3.7-sonnet", id: r, subTitle: "HACKED", subTitleClass: "!opacity-100 gradient-text-high font-bold", _serializableTitle: () => "3.7 Hacked" },
```

This will:
- Add a "HACKED" subtitle 
- Apply the same gradient styling as the "MAX" version
- Make the text bold
- Show "3.7 Hacked" in dropdowns and model selection UI elements

#### Alternative Styling Options

If you want to use red text instead of the gradient:
```js
a = { ...e, title: "claude-3.7-sonnet", id: r, subTitle: "HACKED", subTitleClass: "!opacity-100 text-red-600 font-bold", _serializableTitle: () => "3.7 Hacked" },
```

For animation effects (may not work in all Cursor versions):
```js
a = { ...e, title: "claude-3.7-sonnet", id: r, subTitle: "HACKED", subTitleClass: "!opacity-100 text-red-500 animate-pulse font-bold", _serializableTitle: () => "3.7 Hacked" },
```

## 4. Combined Modifications: Ultimate Claude Setup

For the ultimate setup that combines all modifications, follow these steps in order:

1. First, create a backup of your `workbench.desktop.main.js` file
2. Apply the token limit modification to enable 200K context
3. Apply the thinking level modification to always use high-level thinking
4. Apply the UI customization to make Claude 3.7 stand out

### Example of All Modifications Together:

```js
// 1. Modify getEffectiveTokenLimit
async getEffectiveTokenLimit(e) {
  return 200000; // 200K token limit for all models
  
  // Original code below will be skipped
  const n = e.modelName;
  // ...
}

// 2. Modify getModeThinkingLevel
getModeThinkingLevel(e) {
  return "high";
}

// 3. Modify UI component
a = { ...e, title: "claude-3.7-sonnet", id: r, subTitle: "HACKED", subTitleClass: "!opacity-100 gradient-text-high font-bold", _serializableTitle: () => "3.7 Hacked" },
```

## How to Find Files After Cursor Updates

If Cursor updates and file paths change, use these commands to locate the right files:

```bash
# Find the workbench.desktop.main.js file
find /path/to/cursor -name "workbench.desktop.main*.js"

# Search for getEffectiveTokenLimit function
grep -n "getEffectiveTokenLimit" [path-to-file]

# Search for getModeThinkingLevel function
grep -n "getModeThinkingLevel" [path-to-file]

# Search for claude-3.7-sonnet styling
grep -n "title: \"claude-3.7-sonnet\"" [path-to-file]
```

## Automated Modification with Python

For an automated approach, you can use the included Python tool in the `cursor_modifier` directory:

1. Run `python cursor_claude_modifier.py` or use the batch files (`run_modifier.bat` for Windows, `run_modifier.sh` for Linux/Mac)
2. The tool will:
   - Locate the Cursor installation
   - Find the relevant JavaScript files
   - Create backups of original files
   - Apply the selected modifications
   - Show you a diff of the changes before applying them

## Warning and Known Issues

1. **Updates Override Changes**: Cursor updates will likely overwrite these modifications. You'll need to reapply them after updates.

2. **No Server-Side Changes**: These modifications only affect the client-side code. The actual token usage is still controlled by Anthropic's API, so you may encounter server-side limitations.

3. **UI Limitations**: 
   - Some UI modifications may not appear exactly as expected due to CSS interactions
   - The gradient styling may render differently in different themes
   - Animation effects may not work in all versions of Cursor

4. **API Key Requirements**: These modifications don't bypass any API key requirements. If you're using your own API key, costs are still determined by Anthropic's pricing.

5. **Thinking Level Impact**: Setting thinking level to "high" will make Claude show more of its reasoning process, which may increase token usage.

## Technical Implementation Details

### Token Limit Implementation
- The token limit is controlled by the `getEffectiveTokenLimit` function
- This function first checks a cache, then calls an API, and falls back to default limits
- By modifying this function, we bypass the API call and directly set our preferred limit

### Thinking Level Implementation
- The thinking level is controlled by the `getModeThinkingLevel` function
- Thinking levels include "none" (default), "medium", and "high"
- The `getThinkingLevel` function converts string values to enum constants used internally

### UI Styling Implementation
- Model UI is controlled by style objects with properties like `title`, `subTitle`, `subTitleClass`
- The `_serializableTitle` function controls how the model appears in dropdowns
- CSS classes like `gradient-text-high` create the premium gradient effect seen in the MAX version

Remember to make backups before making changes. These modifications affect only the local client and don't change Claude's actual capabilities or underlying API interactions.