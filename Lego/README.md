Make your app Material data
===========================

[`Generator.py`](https://github.com/Protino/dump/blob/master/Lego/generator.py) provides ways to alter [default data](dl.dropboxusercontent.com/u/231329/xyzreader_data/data.json) provided by Udacity. The code is very self-explanatory, I've added comments wherever neccessary. You can alter the data using the variables `titles`,`names` (image file name), `aspect_ratios` etc. After editing the data you must commit the changes and push. Now you can run `test_endpoint()` method to verify results.

To use the new data, set `url` to `https://raw.githubusercontent.com/<USER_NAME>/<REPO_NAME>/<SUB_FOLDER_IF_ANY>/master/data.json` in config.class` at `remote` package. You cannot edit a lot as it is tightly coupled with the android client.


##### TODO
* Use [GitPython](https://github.com/gitpython-developers/GitPython) to push changes via code 



