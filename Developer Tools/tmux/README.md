# Tmux

Tmux is a powerful, open-source terminal multiplexer for Unix-like systems that allows users to manage multiple terminal sessions within a single window or remote session.

### Installation on Linux
```bash
sudo apt install tmux
```

### Features of Tmux

1. **Session Management**:
   - **Multiple Sessions**: Tmux allows the creation and management of multiple independent sessions. Each session can have its own windows and panes.
   - **Attach/Detach**: You can detach from a session, leaving tasks running in the background, and later reattach from any terminal, including remotely.

2. **Window Management**:
   - **Multiple Windows**: Within a tmux session, you can create several windows, each running a separate program or shell. Think of them as browser tabs.
   - **Window Navigation**: Easily switch between windows using shortcuts (`Ctrl + b` then `n` for next, `Ctrl + b` then `p` for previous) or by selecting them by number.

3. **Pane Management**:
   - **Split Panes**: Split windows horizontally (`Ctrl + b` then `%`) or vertically (`Ctrl + b` then `"`). Each pane operates as an independent terminal inside the same window.
   - **Pane Navigation**: You can switch between panes (`Ctrl + b` then arrow keys) and resize them as needed.

4. **Customizable Key Bindings**:
   - Tmux lets you personalize key bindings through the configuration file (`~/.tmux.conf`), so you can tailor tmux to your preferred workflow.

5. **Persistence and Recovery**:
   - Tmux sessions can continue running in the background even if you disconnect or your terminal crashes. You can reconnect later and pick up right where you left off.

6. **Scripting and Automation**:
   - Tmux can be scripted to automate tasks such as creating new windows, switching panes, or resizing windows. This is ideal for complex or repetitive workflows.

7. **Session Sharing**:
   - Tmux allows multiple users to connect to the same session over SSH. This feature is useful for collaboration, such as pair programming, where both users can interact with the same terminal session in real time.

8. **Status Bar**:
   - Tmux features a status bar that displays helpful information like session name, current window, time, and battery status. You can customize it with plugins or your own settings.

9. **Search Functionality**:
   - Tmux allows you to search through the output in your windows and panes. Use `Ctrl + b` then `[` to enter search mode.

10. **History and Scrollback**:
    - Each tmux pane has a history buffer, allowing you to scroll back and review previous outputs—even after disconnecting. You can adjust the buffer size to store more lines.

11. **Copy Mode**:
    - Tmux has a copy mode (`Ctrl + b` then `[`) that lets you scroll, select, and copy text from the terminal window. You can navigate through the content and copy as needed.

12. **Plugins and Extensions**:
    - Tmux supports plugins to extend its functionality. Notable plugins include **tmux-resurrect** (for saving and restoring sessions) and **tmuxinator** (for managing tmux projects).

### Use Cases of Tmux

1. **Remote Session Management**:
   - Tmux is invaluable when working remotely over SSH. Even if your connection is lost, you can detach from the session and reconnect later without losing any progress.

2. **Simultaneous Task Management**:
   - Split your terminal into multiple panes to run different tasks concurrently (e.g., monitoring logs, running servers, editing files) all within a single terminal window.

3. **Persistent Sessions**:
   - Tmux is perfect for long-running processes that need to continue even after you disconnect. For example, you can leave a build or test process running in the background.

4. **Collaboration**:
   - Tmux enables real-time collaboration by allowing multiple users to share the same session over SSH. Everyone can view and interact with the terminal session simultaneously.


### Difference between **session, window and pane**

| Feature        | Session                                                                 | Window                                                                 | Pane                                                                                             |
|----------------|------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **Definition** | A collection of windows, representing a workspace or project.          | A workspace within a session, similar to a tab in a browser.           | A subdivision of a window, created by splitting it either horizontally or vertically.            |
| **Purpose**     | To separate different tasks or projects, allowing for organized workflows. | To organize different tasks or applications within a session.          | To run multiple terminal applications side by side within a single window.                       |
| **Structure**   | Contains one or more windows.                                           | Contains one or more panes.                                             | Operates as an independent terminal within its parent window.                                     |
| **Identification** | Identified by a name or number.                                        | Identified by a number and can be named for easier reference.          | Identified by a number within its parent window.                                                  |
| **Creation**    | Created using the `tmux new-session` command or by pressing `Ctrl+b c`. | Created using the `new-window` command or by pressing `Ctrl+b c`.      | Created by splitting an existing window using `Ctrl+b %` (horizontal split) or `Ctrl+b "` (vertical split). |
| **Navigation**  | Switch between sessions using `tmux switch-client -t <session-name>` or `Ctrl+b s`. | Switch between windows using `Ctrl+b n` (next) or `Ctrl+b p` (previous). | Move between panes using `Ctrl+b` followed by arrow keys. |
| **Use Case**    | Ideal for separating different projects or tasks, such as "Work" and "Personal." | Useful for separating different tasks or applications within a session, like "Code," "Logs," and "Build." | Useful for monitoring multiple outputs or running related tasks simultaneously within a single window. |



### Some Cheatsheet command for TMUX

| **Command**                                      | **Description**                                              |
|--------------------------------------------------|--------------------------------------------------------------|
| `tmux`                                           | Start a new TMUX session.                                     |
| `tmux new-session -s session_name`                | Start a new session with a custom name.                       |
| `tmux attach`                                    | Attach to the last used session.                              |
| `tmux attach -t session_name`                     | Attach to a specific session by name.                         |
| `tmux detach`                                    | Detach from the current session.                              |
| `Ctrl + b, c`                                    | Create a new window in the current session.                   |
| `Ctrl + b, n`                                    | Switch to the next window.                                    |
| `Ctrl + b, p`                                    | Switch to the previous window.                                |
| `Ctrl + b, %`                                    | Split the window vertically.                                  |
| `Ctrl + b, "`                                    | Split the window horizontally.                                |
| `Ctrl + b, x`                                    | Close the current pane.                                       |
| `Ctrl + b, o`                                    | Switch between panes.                                         |
| `Ctrl + b, z`                                    | Toggle zoom for the current pane (maximize pane).             |
| `Ctrl + b, &`                                    | Close the current window.                                     |
| `tmux kill-session -t session_name`              | Kill a specific session by name.                              |
| `tmux list-sessions`                             | List all existing TMUX sessions.                              |
| `tmux rename-session -t old_name new_name`       | Rename an existing session.                                   |
| `Ctrl + b, d`                                    | Detach from the current session.                              |
| `tmux list-windows`                              | List all windows in the current session.                      |
| `Ctrl + b, ,`                                    | Rename the current window.                                    |
| `Ctrl + b, w`                                    | List all windows in the current session (for quick navigation). |
| `tmux send-keys 'command' C-m`                   | Send keys/commands to the current pane (useful for automation).|
| `tmux split-window -v`                           | Split the window vertically.                                  |
| `tmux split-window -h`                           | Split the window horizontally.                                |
| `tmux resize-pane -D`                            | Resize the current pane down.                                 |
| `tmux resize-pane -U`                            | Resize the current pane up.                                   |
| `tmux resize-pane -L`                            | Resize the current pane left.                                 |
| `tmux resize-pane -R`                            | Resize the current pane right.                                |
| `tmux list-panes`                                | List all panes in the current window.                         |
| `tmux setw -g mode-keys vi`                      | Switch key bindings to vi style (useful for vim users).       |
| `tmux show-options`                              | Show all the current session options.                         |
| `tmux set-option -g status-left "Custom text"`    | Customize the status line with text or information.           |

**Note**: `Ctrl + b, c` means to first press <kbd>Ctrl</kbd> + <kbd>b</kbd>, then release both keys. Afterward, press <kbd>c</kbd>.

Sample file for the configuring tmux: [~/.tmux.conf](./.tmux.conf)

### References:

- [Tmux Wiki on GitHub](https://github.com/tmux/tmux/wiki)
- [Red Hat's Beginner's Guide to Tmux](https://www.redhat.com/en/blog/introduction-tmux-linux)
- [Tmux Cheatsheet](https://tmuxcheatsheet.com/)
- [Windows Session and Pane Workflow in Tmux](https://coderwall.com/p/_g2vpq/workflow-in-tmux)
- [Configuring Tmux - GitHub Wiki](https://github.com/tmux/tmux/wiki/Getting-Started#configuring-tmux)