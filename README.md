# NonsenseBot
Simple discord bot to throw out random files from a directory as well as handle FATE dice rolls.

# What's this?

This is a bot I've designed for personal use. It fulfills two simple functions and doesn't bother with more than that. Configurations are loaded in via json and an example configuration file is available in the repository.


# What's it do?

Because the bot was made in a short amount of time, and because the requirements were so simple, it only has two functions, which it faithfully performs on a private server.

## Roll dice

Specifically, FATE dice. It rolls them and by default, outputs an emoji for each one, sorted - Plus, Blank, or Minus. `!roll 4` will get you four dice, simple as that.

## Nonsense

This was really the point of making our own bot: Once every four hours, you can simply type `!nonsense` to be given a random link to a file from the list. The file list is around 300 different random videos at the time of initial upload.

## Is that all?

That's all. It's not changing the world, but it's exactly what I needed.

# How can I use it?
If you really want this exact thing on your discord server, you will need to edit the configuration file to include your secret token and a list of files in your "nonsense" directory. If it's not in the config, it won't be chosen. Because these are web links,  the bot can put them out quickly without worrying about upload bandwidth to discord, but that also means you should probably have some sort of index.html on the site to avoid someone scraping all of your files too easily.

Once you've set the config, simply run it as normal with Python 3.5 or above and the latest version of [Discord.Py Rewrite](https://discordpy.readthedocs.io/en/rewrite/).
