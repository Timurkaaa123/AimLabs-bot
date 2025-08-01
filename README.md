# AimLabs-Bot

A bot that uses computer vision to aim in the game AimLabs

---------

# Installation
1. Clone the repository
```
git clone https://github.com/Timurkaaaaaaa/AimLabs-bot.git
```
2. Create a virtual environment
```
python3 -m venv .venv
```
3. Activate the virtual environment
```md
# Windows
.venv/scripts/activate

# Linux/MacOS
source .venv/bin/activate
```
4. Download the required modules
```
pip install -r requirements.txt
```
6. Download OBS, create a scene with the AimLabs window source and turn on the virtual camera
> [!TIP]
>**Recommended settings:**
>- Output resolution: 1280x720 or less
>- Frame rate: 30 or more
6. Make changes to `config/config.py`
> [!TIP]
> In the AimLabs settings it is recommended to set the sensitivity to 1
7. Run the run.py file
```
python3 run.py
```

----------

# Inspiration
Inspired by [Priler/aimlabbot](https://github.com/Priler/aimlabbot)
