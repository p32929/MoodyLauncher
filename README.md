# MoodyLauncher

A tiny Python script that opens a whole set of apps at once, grouped by "mood". Every time you sit down to code you open the same editor, browser, terminal and notes app one by one. With MoodyLauncher you save that set once as a mood, like *Web Development* or *Gaming*, then pick it from a menu and everything opens together.

## Features

1. **One pick opens many apps:** choose a mood and every app in it starts.
2. **Create moods from the menu:** drag each app into the terminal, then type `0` to save.
3. **Plain text moods:** each mood is a `.txt` file next to the script, one app path per line, so you can also edit it by hand.

## How to use

```bash
python moodyLauncher.py
```

You get a menu like this:

```
0. Stop
1. Create new mood
2. Web Development.txt
3. Gaming.txt
```

1. Type a number to open that mood.
2. Type `1` to make a new mood: give it a name, drag in the apps one at a time, and type `0` when you are done.
3. Type `0` to quit.

> **Python 2 only.** It uses `raw_input()` and the `string-escape` codec, which Python 3 does not have. To run it on Python 3, replace `raw_input()` with `input()` and drop the `.encode('string-escape')` call.

## License

MIT License — Copyright (c) 2019 Fayaz Bin Salam. See [LICENSE](LICENSE) for the full text.

## Contributing

Contributions are very welcome, thank you! Before you start on a pull request, please open an issue and tell me what you would like to add or change. That way we can agree on it first, and your time is not wasted on something that might not fit. Thanks for helping make MoodyLauncher better.

## You might also like

<p><a href="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/0"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/0-dark.svg"><img src="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/0-light.svg" width="50%" align="top" alt="More apps by p32929 on OpenStore (1)"></picture></a><a href="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/1"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/1-dark.svg"><img src="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/1-light.svg" width="50%" align="top" alt="More apps by p32929 on OpenStore (2)"></picture></a><br><a href="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/2"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/2-dark.svg"><img src="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/2-light.svg" width="50%" align="top" alt="More apps by p32929 on OpenStore (3)"></picture></a><a href="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/3"><picture><source media="(prefers-color-scheme: dark)" srcset="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/3-dark.svg"><img src="https://openstore.pfay.workers.dev/more/p32929/moodylauncher/personal/3-light.svg" width="50%" align="top" alt="More apps by p32929 on OpenStore (4)"></picture></a></p>

<p><a href="https://p32929.github.io/share/?repo=MoodyLauncher"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-share-dark.svg"><img src="https://p32929.github.io/readme/footer-share-light.svg" width="50%" align="top" alt="Share this project with your friends in one click"></picture></a><a href="https://p32929.github.io/support/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-support-dark.svg"><img src="https://p32929.github.io/readme/footer-support-light.svg" width="50%" align="top" alt="If you like my work and want to support me, feel free to support"></picture></a><br><a href="https://openstore.pfay.workers.dev/add"><picture><source media="(prefers-color-scheme: dark)" srcset="https://p32929.github.io/readme/footer-join-dark.svg"><img src="https://p32929.github.io/readme/footer-join-light.svg" width="100%" align="top" alt="Put your own apps on OpenStore: free, your listing lives in your own repo"></picture></a></p>
