# TeacherAI

TeacherAI aims to provide engaging and effective feedback on guitar excercises in order to develop playing ability.

## Setup
### Pip install
The package will be pip-installable. Run
```
pip install TeacherAI
```
### Audio Source
An audio interface such as a Focusrite Scarlett is recommended for optimal performance. Once set up, one could either use a line-in input or mic an amp. To view the avaliable audio sources, whilst in the root directory, run the following command

```
python -m get_audio_source
```

This will display the list of avaliable audio inputs and their respective IDs. To use a certain audio input, in `configs.json`, change the setting `InputDeviceID` to the ID of the device you wish to use.

### Recommended Guitar Settings


## License
Distrubuted under the MIT license.
## Feedback

# Modules
## Fretboard Trainer
Based on Brandon D'Eon's excercise for memorising the notes of the fretboard (see [here](https://www.youtube.com/watch?v=7PMZWb6ZNJc&t=180s&pp=ygUjYnJhbmRvbiBkZW9uIG5vdGVzIG9mIHRoZSBmcmV0Ym9hcmQ%3D)), this script will test your memorisation of the notes of each string. The program will display a note, which the user must play within a certain time frame. The program will then evaluate whether the right note was played. If correct, the next note will be displayed, otherwise, the player can try again. If *hard mode* is enabled, the player will have to begin from the start if they make a mistake.

To start, in the directory `Modules`, pass

```
python -m fretboard_trainer
```

### Settings
- Pass `-hm` or `--hardmode` to toggle hardmode.


### Future Features
- Play both notes on each string
- Specify string and hence frequencies (D5 for example)

## Rhythm Trainer
Coming Soon



