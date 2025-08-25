# Claude Customization Instructions

This document provides instructions for customizing Claude 3.7 in Cursor. These modifications are UI-only and don't affect functionality.

## 1. Always Set Claude's Thinking Level to High

### Step 1: Locate the getModeThinkingLevel Function
In the `workbench.desktop.main.js` file, locate the `getModeThinkingLevel` function by searching for:
```js
getModeThinkingLevel(e) {
  return this.getAllModes().find((n) => n.id === e)?.thinkingLevel ?? "none";
}
```

### Step 2: Replace with Always High
Replace it with:
```js
getModeThinkingLevel(e) {
  return "high";
}
```

## 2. Make Claude 3.7 Regular Appear as "3.7 Hacked" with Red Styling

### Step 1: Locate the UI Definition
Find where the Claude 3.7 regular model is styled. Search for:
```js
a = { ...e, title: "claude-3.7-sonnet", id: r, _serializableTitle: () => "claude-3.7-sonnet" },
```

### Step 2: Modify the UI Component
Replace with:
```js
a = { ...e, title: "claude-3.7-sonnet", id: r, subTitle: "HACKED", subTitleClass: "!opacity-100 text-red-500 animate-pulse font-bold", _serializableTitle: () => "3.7 Hacked" },
```

If the animation doesn't work or only the subtitle shows, try these alternative solutions:

### Option 1: Use a Custom Subtitle Element
Look for code that handles the MAX version and modify the regular version similarly:
```js
a = {
  ...e,
  title: "claude-3.7-sonnet",
  id: r,
  subTitle: "HACKED",
  subTitleClass: "!opacity-100 text-red-600 font-bold",
  customSubTitle: (() => {
    var elem = document.createElement('span');
    elem.textContent = "HACKED";
    elem.style.color = "red";
    elem.style.animation = "pulse 2s infinite";
    elem.style.fontWeight = "bold";
    return elem;
  })(),
  _serializableTitle: () => "3.7 Hacked"
},
```

### Option 2: Add a CSS Keyframe Animation
If your custom animation doesn't work, also add this CSS somewhere in the page:
```css
@keyframes pulse {
  0% { opacity: 0.6; }
  50% { opacity: 1; }
  100% { opacity: 0.6; }
}
```

### Option 3: Use Gradient Text Like MAX
If red text doesn't show up, use the same gradient approach as MAX but with red tones:
```js
a = {
  ...e,
  title: "claude-3.7-sonnet",
  id: r,
  subTitle: "HACKED",
  subTitleClass: "!opacity-100 gradient-text-high font-bold",
  _serializableTitle: () => "3.7 Hacked"
},
```

## How to Find Files After Updates

If Cursor updates and file paths change, use these commands to locate the right files:

```bash
# Find the workbench.desktop.main.js file
find /mnt/c/Users/aleja/AppData/Local/Programs/cursor -name "workbench.desktop.main*.js"

# Search for getModeThinkingLevel function
grep -n "getModeThinkingLevel" [path-to-file]

# Search for claude-3.7-sonnet styling
grep -n "title: \"claude-3.7-sonnet\"" [path-to-file]
```

Remember to make backups before making changes. These modifications only affect the UI and don't change Claude's functionality.