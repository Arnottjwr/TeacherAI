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

**MacOS**
```python
python -m get_audio_source
```
**Ubuntu**
```
python -m get_audio_source.py
```
This will display the list of avaliable audio inputs and their respective IDs. To use a certain audio input, in `configs.json`, change the setting `InputDeviceID` to the ID of the device you wish to use.

### Recommended Guitar Settings

## Modules
### Fretboard Trainer


### Rhythm Trainer
Coming Soon