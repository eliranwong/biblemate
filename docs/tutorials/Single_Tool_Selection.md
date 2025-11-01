# 🔧 Single Tool Selection

In some cases, you may want to specify a particular tool for a simple task, rather than having multiple tools automatically selected in the fully automatic `agent mode`.

You can specify a single tool by prefixing a tool name with `@` at the beginning of your prompt. For example,

```
@retrieve_bible_cross_references Deut 6:4; John 3:16
```

Watch this video: https://youtu.be/50m1KRj6uhs

BibleMate AI can also automatically select a single tool to address your request. Simply begin your request with `@` followed by a space, instead of specifying a tool name. For example,

```
@ Read Deut 6:4; John 3:16
```

## Auto Tool Selection

In `agent` and `partner` modes, tools are automatically selected by default.

In `mode` mode, you can enter `.autotool` or `Esc+T` to toggle auto tool selection. With this feature enabled, you don't need to manually prefix your request with `@ `.