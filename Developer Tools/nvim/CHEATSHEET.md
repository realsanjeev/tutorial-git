## **Neovim Commands Cheatsheet**

| **Mode**                        | **Command**                          | **Description**                                      |
|----------------------------------|--------------------------------------|------------------------------------------------------|
| **Normal Mode**                  | `h`, `j`, `k`, `l`                   | Move cursor left, down, up, right                    |
|                                  | `x`                                  | Delete the character under the cursor                |
|                                  | `dd`                                 | Delete the current line                              |
|                                  | `yy`                                 | Copy the current line                                |
|                                  | `p`                                  | Paste after the cursor                               |
|                                  | `u`                                  | Undo last change                                     |
|                                  | `Ctrl + r`                           | Redo last undone change                              |
|                                  | `.` (dot)                            | Repeat the last command                              |
|                                  | `:bnext`                             | Go to the next buffer                                |
|                                  | `:bprev`                             | Go to the previous buffer                            |
|                                  | `:split`                             | Split the window horizontally                        |
|                                  | `:vsplit`                            | Split the window vertically                          |
|                                  | `:tabnew`                            | Open a new tab                                       |
|                                  | `Ctrl + w, w`                        | Switch between open windows                          |
|                                  | `Ctrl + w, q`                        | Close the current window                             |
| **Insert Mode**                  | `Ctrl + h`                           | Delete the character before the cursor               |
|                                  | `Ctrl + w`                           | Delete the word before the cursor                    |
|                                  | `Ctrl + u`                           | Delete everything before the cursor (line)           |
|                                  | `Ctrl + k`                           | Delete the current line after the cursor             |
|                                  | `Ctrl + o`                           | Temporarily return to Normal Mode for one command    |
| **Visual Mode**                  | `v`                                  | Start selecting text character by character          |
|                                  | `V`                                  | Select entire lines                                  |
|                                  | `Ctrl + v`                           | Start block selection (rectangular text)             |
|                                  | `>`                                  | Indent the selected text to the right                |
|                                  | `<`                                  | Indent the selected text to the left                 |
|                                  | `=`                                  | Auto-format the selected text                        |
|                                  | `~`                                  | Change the case of the selected text (uppercase <-> lowercase) |
|                                  | `J`                                  | Join selected lines into one                        |
| **Command Mode (Ex Mode)**       | `:`                                  | Enter Command Mode                                   |
|                                  | `:w`                                 | Save the file                                        |
|                                  | `:q`                                 | Quit Neovim                                          |
|                                  | `:wq`                                | Save and quit the file                               |
|                                  | `:q!`                                | Quit without saving changes                          |
|                                  | `:x`                                 | Save and quit the file (similar to `:wq`)             |
|                                  | `:set number`                        | Show line numbers                                    |
|                                  | `:set nonumber`                      | Hide line numbers                                    |
|                                  | `:syntax enable`                     | Enable syntax highlighting                           |
|                                  | `:syntax off`                        | Disable syntax highlighting                          |
|                                  | `:set paste`                         | Disable auto-indentation (useful for pasting text)   |
|                                  | `:set nopaste`                       | Re-enable normal paste mode                          |
| **Replace Mode**                 | `r`                                  | Replace the character under the cursor               |
|                                  | `R`                                  | Start replacing multiple characters                  |
|                                  | `Ctrl + h`                           | Move the cursor left during replace mode             |
| **Select Mode**                  | `gh`                                 | Enter Select mode                                    |
| **Terminal Mode**                | `:term`                              | Open an embedded terminal                            |
|                                  | `Ctrl + \`, `Ctrl + n`               | Exit terminal mode and return to Normal Mode         |
|                                  | `Ctrl + w, k`                        | Move to the window above in terminal                 |
|                                  | `Ctrl + w, j`                        | Move to the window below in terminal                 |
|                                  | `Ctrl + w, h`                        | Move to the window left in terminal                  |
|                                  | `Ctrl + w, l`                        | Move to the window right in terminal                 |
| **Insert Mode (for Searching)**  | `/` or `?`                           | Start search (forward or backward)                   |
|                                  | `n`                                  | Jump to the next occurrence of the search            |
|                                  | `N`                                  | Jump to the previous occurrence of the search        |
|                                  | `Esc`                                | Cancel the search                                    |
| **Search and Replace**           | `:/pattern`                          | Search for `pattern` forward                         |
|                                  | `:?pattern`                          | Search for `pattern` backward                        |
|                                  | `:%s/old/new/g`                      | Replace all occurrences of `old` with `new` in the entire file |
|                                  | `:s/old/new/g`                       | Replace all occurrences of `old` with `new` in the current line |
|                                  | `:argdo %s/old/new/g`                | Replace in all files in the argument list            |
| **Miscellaneous Commands**       | `:help`                              | Open Neovim’s help documentation                     |
|                                  | `:e filename`                        | Open a file named `filename`                         |
|                                  | `:vsp filename`                      | Open `filename` in a vertical split                  |
|                                  | `:sp filename`                       | Open `filename` in a horizontal split                |
|                                  | `:qa`                                | Quit all windows and Neovim                          |
|                                  | `:tabnew`                             | Open a new tab page                                  |
|                                  | `:b`                                 | Switch between buffers                               |
|                                  | `Ctrl + p`                           | Open the file search dialog (requires `fzf` plugin)  |
|                                  | `:enew`                              | Open a new empty buffer                              |

This table contains **all the modes and commands** you need in Neovim for effective text editing, navigation, and workflow!



### **Buffer and Window Management**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:b#`                   | Switch to the last accessed buffer                   |
| `:b <buffer_name>`      | Switch to a specific buffer by name or number        |
| `:ls`                   | List all open buffers                                |
| `:hide`                 | Hide the current buffer (close without quitting)     |
| `Ctrl + w, s`           | Split window horizontally                           |
| `Ctrl + w, v`           | Split window vertically                             |
| `Ctrl + w, c`           | Close the current window                            |
| `Ctrl + w, o`           | Close all other windows, keep the current one       |
| `Ctrl + w, =`           | Equalize window sizes                               |


### **Text Manipulation**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `gU`                    | Uppercase the current word                           |
| `gu`                    | Lowercase the current word                           |
| `gUaw`                  | Uppercase the word under the cursor                  |
| `guaw`                  | Lowercase the word under the cursor                  |
| `gU$`                   | Uppercase from the cursor to the end of the line     |
| `gu$`                   | Lowercase from the cursor to the end of the line     |
| `Ctrl + t`              | Indent the current line to the right                 |
| `Ctrl + d`              | Indent the current line to the left                  |
| `>>`                    | Indent the current line to the right (Visual mode)   |
| `<<`                    | Indent the current line to the left (Visual mode)    |
| `J`                     | Join the current line with the next one (removes newline) |


### **Search & Navigation**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `/pattern`              | Search for `pattern` forward                         |
| `?pattern`              | Search for `pattern` backward                        |
| `n`                     | Go to the next occurrence of the search              |
| `N`                     | Go to the previous occurrence of the search          |
| `*`                     | Search for the word under the cursor (forward)       |
| `#`                     | Search for the word under the cursor (backward)      |
| `g*`                    | Search for the word under the cursor (forward, ignore case) |
| `g#`                    | Search for the word under the cursor (backward, ignore case) |
| `/%`                    | Jump to the matching parenthesis or bracket          |
| `Ctrl + o`              | Go back to the previous location                     |
| `Ctrl + i`              | Go forward to the next location                      |
| `gg`                    | Jump to the beginning of the file                    |
| `G`                     | Jump to the end of the file                          |
| `{`                     | Jump to the previous paragraph                       |
| `}`                     | Jump to the next paragraph                           |
| `0`                     | Jump to the beginning of the line                    |
| `$`                     | Jump to the end of the line                          |
| `w`                     | Jump to the beginning of the next word               |
| `e`                     | Jump to the end of the current word                  |
| `b`                     | Jump to the beginning of the previous word           |
| `Ctrl + f`              | Scroll one page down                                |
| `Ctrl + b`              | Scroll one page up                                  |
| `Ctrl + u`              | Scroll half a page up                               |
| `Ctrl + d`              | Scroll half a page down                             |


### **Clipboard and Registers**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `"aY`                   | Yank (copy) to register `a`                          |
| `"aP`                   | Paste from register `a`                              |
| `"aD`                   | Delete to register `a`                               |
| `"a"`                   | Access register `a`                                  |
| `"0`                    | Use the unnamed register (yanked text)               |
| `"*`                    | Use the system clipboard register (requires Neovim to be compiled with clipboard support) |
| `"+`                    | Use the system clipboard register for copy-pasting   |


### **Undo & Redo**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:undolist`             | Show the undo history                                |
| `g-`                    | Go to the previous change                           |
| `g+`                    | Go to the next change                               |


### **Macros**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `q<register>`           | Start recording a macro into register `<register>`   |
| `q`                     | Stop recording a macro                               |
| `@<register>`           | Play back a macro from register `<register>`         |
| `@@`                    | Replay the last macro                               |


### **File Operations**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:e <filename>`         | Edit or open a file named `<filename>`               |
| `:w <filename>`         | Write (save) the file to a specific `<filename>`     |
| `:saveas <filename>`    | Save the current file as `<filename>`                |
| `:Explore`              | Open a file explorer (if `netrw` is installed)       |
| `:bdelete`              | Delete the current buffer (close the file)           |
| `:qall`                 | Quit all windows and Neovim                          |
| `:q!`                   | Quit without saving changes                         |
| `:wq`                   | Save and quit the file                               |


### **Window and Tab Management**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:tabnew`               | Open a new tab                                      |
| `:tabn`                 | Go to the next tab                                  |
| `:tabp`                 | Go to the previous tab                              |
| `:tabm <number>`        | Move the current tab to position `<number>`         |
| `Ctrl + w, w`           | Switch between open windows                         |
| `Ctrl + w, h/j/k/l`     | Move focus to the left, down, up, or right window   |
| `Ctrl + w, v`           | Split the window vertically                         |
| `Ctrl + w, s`           | Split the window horizontally                       |
| `Ctrl + w, q`           | Close the current window                            |


### **Syntax & Highlighting**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:syntax enable`        | Enable syntax highlighting                          |
| `:syntax off`           | Disable syntax highlighting                         |
| `:set syntax=<type>`    | Set syntax highlighting for specific file type (e.g., `python`, `html`) |


### **Other Useful Commands**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:set number`           | Show line numbers                                    |
| `:set nonumber`         | Hide line numbers                                    |
| `:set relativenumber`   | Show relative line numbers                           |
| `:set nowrap`           | Disable line wrapping                                |
| `:set wrap`             | Enable line wrapping                                 |
| `:set ignorecase`       | Ignore case while searching                          |
| `:set noignorecase`     | Enable case-sensitive search                        |
| `:set tabstop=4`        | Set the tab width to 4 spaces                        |
| `:set shiftwidth=4`     | Set the indentation width to 4 spaces                |


Here are even more **Neovim** commands, covering a range of functionality from advanced navigation to customization and debugging tools:


### **Search and Replace (Advanced)**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:%s/pattern/replace/gc` | Replace all occurrences of `pattern` with `replace` globally and ask for confirmation |
| `:argdo %s/pattern/replace/g` | Replace `pattern` with `replace` in all files in the argument list |
| `:v/regex/pattern/`     | Perform a search and highlight matches without moving the cursor |
| `:g/regex/pattern/d`    | Delete all lines matching the regex pattern         |


### **Customizing Neovim (Settings)**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:set background=dark`  | Set dark background theme                            |
| `:set background=light` | Set light background theme                           |
| `:set tabstop=4`        | Set tab width to 4 spaces                            |
| `:set shiftwidth=4`     | Set indentation width to 4 spaces                    |
| `:set expandtab`        | Convert tabs to spaces                               |
| `:set noexpandtab`      | Use real tabs instead of spaces                      |
| `:set autoindent`       | Automatically indent new lines                       |
| `:set smartindent`      | Enable smart indentation                             |
| `:set incsearch`        | Show incremental search results as you type          |
| `:set hlsearch`         | Highlight search results                             |
| `:set wrap`             | Wrap long lines to fit within the window             |
| `:set nowrap`           | Disable line wrapping                                |
| `:set relativenumber`   | Display relative line numbers                        |
| `:set number`           | Display absolute line numbers                        |
| `:set mouse=a`          | Enable mouse support in all modes                    |
| `:set clipboard=unnamed`| Use the unnamed clipboard for copying and pasting    |
| `:set clipboard=unnamedplus` | Use the system clipboard for copy-pasting       |


### **Window and Split Management**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `Ctrl + w, w`           | Switch between open windows                         |
| `Ctrl + w, q`           | Close the current window                            |
| `Ctrl + w, t`           | Open a new tab in the current window                 |
| `Ctrl + w, r`           | Rotate through windows in a counter-clockwise manner|
| `Ctrl + w, R`           | Rotate through windows in a clockwise manner        |
| `Ctrl + w, h/j/k/l`     | Move to the window on the left, down, up, or right   |
| `Ctrl + w, =`           | Make all windows equal in size                      |
| `Ctrl + w, _`           | Maximize the current window                         |
| `Ctrl + w, |`           | Maximize the current window horizontally            |
| `Ctrl + w, -`           | Maximize the current window vertically              |
| `Ctrl + w, +`           | Increase the size of the current window             |
| `Ctrl + w, -`           | Decrease the size of the current window             |
| `:sp filename`          | Open a file in a horizontal split                   |
| `:vsp filename`         | Open a file in a vertical split                     |


### **Advanced Editing**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `Ctrl + x, Ctrl + o`    | Autocomplete word based on context                   |
| `Ctrl + x, Ctrl + i`    | Autocomplete from available snippets                 |
| `Ctrl + r, Ctrl + f`    | Autocomplete from files in the current directory     |
| `:%s/foo/bar/gi`        | Perform a global case-insensitive replace across the whole file |
| `gv`                    | Reselect the previously selected text                |
| `C`                     | Change the current line (deletes and enters Insert mode) |
| `D`                     | Delete from the cursor to the end of the line        |
| `S`                     | Delete the current line and enter Insert mode        |
| `Ctrl + n`              | Autocomplete for file names and paths                |


### **Macros**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `q<register>`           | Start recording a macro into register `<register>`   |
| `q`                     | Stop recording a macro                               |
| `@<register>`           | Play back a macro from register `<register>`         |
| `@@`                    | Replay the last macro                               |
| `:let @a="Hello"`       | Set register `a` with the string "Hello"             |
| `:let @a=@b`            | Copy the contents of register `b` to register `a`    |


### **Marks and Jumps**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `m<letter>`             | Set a mark at the cursor position using the letter `<letter>` |
| `'a`                    | Jump to the beginning of the line of mark `a`        |
| `` `a ``                | Jump to the exact position of mark `a`               |
| `:marks`                | List all marks in the current buffer                 |
| `Ctrl + o`              | Jump to the previous jump location                   |
| `Ctrl + i`              | Jump to the next jump location                       |


### **Neovim Plugins (Common Plugin Commands)**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:PlugInstall`          | Install plugins (for Vim-Plug plugin manager)        |
| `:PlugUpdate`           | Update installed plugins                             |
| `:PlugClean`            | Remove unused plugins (with Vim-Plug)                |
| `:PackerSync`           | Sync plugins (for Packer plugin manager)             |
| `:PackerInstall`        | Install plugins (for Packer plugin manager)          |
| `:PackerUpdate`         | Update installed plugins (for Packer)                |
| `:Telescope find_files` | Search for files using Telescope plugin              |
| `:Telescope live_grep`  | Search for text in files using Telescope plugin      |
| `:Telescope buffers`    | List open buffers with Telescope                     |


### **Miscellaneous**
| **Command**             | **Description**                                      |
|-------------------------|------------------------------------------------------|
| `:messages`             | Show the message history                             |
| `:checkhealth`          | Check Neovim's health and report errors or warnings  |
| `:version`              | Show Neovim version information                      |
| `:chdir <dir>`          | Change the current working directory to `<dir>`      |
| `:terminal`             | Open an embedded terminal within Neovim             |
| `:q`                    | Quit Neovim                                          |
| `:qa!`                  | Quit Neovim without saving changes                   |
