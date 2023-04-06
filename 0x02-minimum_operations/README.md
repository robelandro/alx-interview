# 0x01. Lockboxes

## 💡 idea

Imagine you have a bunch of boxes that are locked with different keys. Each box has a number on it, from 0 to n - 1, where n is the total number of boxes. For example, if you have 5 boxes, they will be numbered 0, 1, 2, 3 and 4.

Inside each box, there may be some keys that can open other boxes. The keys also have numbers on them, and they match the numbers of the boxes they can open. For example, if you find a key with number 2 inside box 0, that means you can use that key to open box 2.

However, not every box has a key inside it, and not every key has a matching box. For example, you may find a key with number 6 inside box 1, but there is no box 6. Or you may find an empty box with no keys inside it.

You start with the first box (box 0) already unlocked. You want to know if you can open all the other boxes using the keys you find inside the boxes.

### 📝 instructions

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- `boxes` is a list of lists

### 🧪 test cases

```
$ ./0-main.py
```
