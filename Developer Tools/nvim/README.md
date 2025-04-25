## Neovim

Neovim is an open-source, highly configurable text editor that serves as a modern refactor of Vim, aiming to enhance its functionality and maintainability. It retains Vim's core features while introducing improvements such as built-in Language Server Protocol (LSP) support, asynchronous I/O, and enhanced Lua scripting capabilities.

### Getting Started with Neovim
> For installation on Windows and macOS, see the [official installation guide](https://github.com/neovim/neovim/blob/master/INSTALL.md).

**To install Neovim on Debian or Ubuntu:**

```bash
sudo apt-get install neovim
```

**Note**: If you want the latest version of Neovim (e.g., for configuring with [NvChad](https://nvchad.com/)), the above method won't install the latest release. In that case, use the [AppImage (universal Linux package)](https://github.com/neovim/neovim/blob/master/INSTALL.md#appimage-universal-linux-package).

**To download the latest Neovim version via AppImage:**

```bash
# Download the Neovim AppImage
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux-x86_64.appimage
chmod u+x nvim-linux-x86_64.appimage
./nvim-linux-x86_64.appimage
# Expose Neovim globally
mkdir -p /opt/nvim
mv nvim-linux-x86_64.appimage /opt/nvim/nvim
```

Then, add the following line to your shell configuration (`~/.bashrc`, `~/.zshrc`, etc.) and restart your shell:

```bash
export PATH="$PATH:/opt/nvim/"
```

Now you can run Neovim with:

```bash
nvim <filename>
```

### Neovim Modes Overview

1. **Normal Mode (Command Mode)**
   - **Purpose**: This is the default mode when you open Neovim. In this mode, you can navigate text, delete, copy, paste, and perform various operations.
   - **How to Enter**: Press `Esc` from any other mode to return to Normal mode.
   
   **Common Commands in Normal Mode**:
   - Move cursor: `h` (left), `j` (down), `k` (up), `l` (right)
   - Delete a character: `x`
   - Delete a line: `dd`
   - Copy a line: `yy`
   - Paste: `p`
   - Undo changes: `u`
   - Redo changes: `Ctrl + r`

2. **Insert Mode**
   - **Purpose**: Used for typing and editing text. In Insert mode, all keystrokes are inserted as text.
   - **How to Enter**: Press `i` (insert before the cursor), `I` (insert at the beginning of the line), `a` (insert after the cursor), or `A` (insert at the end of the line).
   - **How to Exit**: Press `Esc` to return to Normal mode.

3. **Visual Mode**
   - **Purpose**: Used for selecting text. Once text is selected, you can copy, cut, or format the selection.
   - **How to Enter**: 
     - Press `v` to select text character by character.
     - Press `V` to select entire lines.
     - Press `Ctrl + v` for block selection (select a rectangular block of text).
   - **How to Exit**: Press `Esc` to return to Normal mode.

   **Common Commands**:
   - Copy selected text: `y`
   - Cut selected text: `d`
   - Paste: `p`

4. **Command Mode (Ex Mode)**
   - **Purpose**: Allows you to enter commands for actions like saving, quitting, searching, replacing, and more. These commands are preceded by a colon (`:`).
   - **How to Enter**: Press `:` in Normal mode.
   - **How to Exit**: Press `Esc` to return to Normal mode.
   
   **Common Commands**:
   - Save the file: `:w`
   - Quit Neovim: `:q`
   - Save and quit: `:wq`
   - Force quit without saving: `:q!`
   - Search for a term: `:/<term>`
   - Replace a word: `:s/old/new/g`

5. **Replace Mode**
   - **Purpose**: Lets you replace existing characters with new ones as you type.
   - **How to Enter**: Press `R` in Normal mode and begin typing to replace characters. Multiple characters can be replaced at once.
   - **How to Exit**: Press `Esc` to return to Normal mode.

6. **Select Mode**
   - **Purpose**: Similar to Visual mode, but offers a more intuitive selection behavior like other text editors. It allows you to select text using the arrow keys.
   - **How to Enter**: Press `gh` in Normal mode.
   - **How to Exit**: Press `Esc` to return to Normal mode.

7. **Insert Mode (with Line Numbers)**
   - **Purpose**: This mode allows you to see line numbers while typing for easier navigation and reference.
   - **How to Enter**: Press `Ctrl + G` to toggle line numbers while in Insert mode.

8. **Terminal Mode (Embedded Terminals)**
   - **Purpose**: This mode enables you to interact with an embedded terminal within Neovim.
   - **How to Enter**: Use the `:term` command to open a terminal inside Neovim.
   - **How to Exit**: Press `Ctrl + \`, then `Ctrl + n` to return to Normal mode.

9. **Insert Mode (for Searching)**
   - **Purpose**: When you perform a search using `/` or `?`, this mode allows you to type your search query.
   - **How to Enter**: Type `/` or `?` followed by your search term.
   - **How to Exit**: Press `Esc` to cancel the search.


### Configure the Neovim
Neovim stores its configuration in:
- Linux/macOS: `~/.config/nvim/init.lua` or `~/.config/nvim/init.vim`
- Windows: `C:\Users\YourUser\AppData\Local\nvim\init.lua`

If tbe folder doesn't exists, create it:
```bash
mkdir -p ~/.config/nvim
touch ~/.config/nvim/init.lua
```
### References:
- [Vim Official Website](https://www.vim.org/)
- [Neovim Official Repository](https://github.com/neovim/neovim)
- [NvChad Official Website](https://nvchad.com/)
