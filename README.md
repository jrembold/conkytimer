# conkytimer
A simple toggle-able countdown timer overlay using conky.

## Installation
You should just be able to clone the repository to whatever location you like, and then change the "folder" variable in `toggle_cd` to reflect that folder. Then assign `toggle_cd` to a shortcut key using whatever method you prefer. For i3 I have something like
```
bindsym $mod+F12 exec "<path to toggle_cd>"
```

## Config
 - The timer defaults to 5 minutes whenever the shortcut key is pressed. To change this just adjust the value in `toggle_cd` (in seconds).
 - The timer is set to turn red when out of time. This can be adjusted in the python script by writing out a different `${color }` value in the final print statement.
 - I generally want this showing up on my second monitor, so the `xenerama_head` value is set to 2 in the `timer_rc` conky config file. Change to 0 or 1 to get things on the monitor you prefer.
