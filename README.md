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

## Share

<a href="https://p32929.github.io/share/?repo=MoodyLauncher"><img src="https://p32929.github.io/readme/share.svg" alt="Share this with your friends in just a click" width="420"></a>

## Support

<a href="https://p32929.github.io/support/"><img src="https://p32929.github.io/readme/support.svg" alt="If you like my works and want to support me, feel free to support" width="420"></a>
