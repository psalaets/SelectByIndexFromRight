# SelectByIndexFromRight

Switch to a tab by number, counting from the right.

## Keyboard shortcuts

### OS X

Tab | Shortcut | Note
----|----------|-----
Last|<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>1</kbd>
2nd to last|<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>2</kbd>
3rd to last|<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>3</kbd>| See [Gotchas on OS X](#gotchas-on-os-x)
4th to last|<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>4</kbd>| See [Gotchas on OS X](#gotchas-on-os-x)
...|...
9th to last|<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>9</kbd>

### Linux, Windows

> Apparently alt+shift+1 through alt+shift+5 are already taken by default in Sublime. Avoid this package unless you want to resolve the key command conflicts :(

Tab | Shortcut | Note
----|----------|-----
Last|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>1</kbd>| See comment above
2nd to last|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>2</kbd>| See comment above
3rd to last|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>3</kbd>| See comment above
4th to last|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>4</kbd>| See comment above
5th to last|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>5</kbd>| See comment above
...|...
9th to last|<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>9</kbd>

## Gotchas on OS X

<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>3</kbd> and <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>4</kbd> are OS X keyboard shortcuts for taking screenshots.

### Workaround 1: Change this package's shortcuts

In Sublime go to:

`Preferences | Package Settings | SelectByIndexFromRight | Key Bindings - Default`

and copy only the key command objects (everything in there except the outer array). Then go to

`Preferences | Package Settings | SelectByIndexFromRight | Key Bindings - User`

and paste into the array. Then edit as necessary.

### Workaround 2: Change OS X screenshot shortcuts

In OS X go to:

`System Preferences | Keyboard | Shortcuts | Screen Shots`
