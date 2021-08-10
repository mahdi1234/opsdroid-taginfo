# opsdroid skill taginfo

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to get https://taginfo.openstreetmap.org/ data.


## Usage

#### `&tg highway=steps`
#### `&tg highway=*`


> user: you check check steps like this &tg highway=steps

> opsdroid: 
>
>           ### Occurence of highway=steps ###
>           all --> 19448
>           nodes --> 49
>           ways --> 19399
>           relations --> 0
>
>           ### and most common tag combinations ###
>
>           incline:* --> 7012
>           source:* --> 4112
>           surface:* --> 3920
>           lit:* --> 2445
>           lit:yes --> 1803
>           source:survey --> 1049
>           surface:paving_stones --> 1006

> user: or all highway values &tg highway=*

> opsdroid: 
>
>           ### Occurence of highway=* ###
>           track --> 328399
>           residential --> 242353
>           footway --> 225501
>           service --> 223741
>           path --> 118836
>           tertiary --> 73005
>           crossing --> 46817
>           secondary --> 40849
>           bus_stop --> 40490
>           unclassified --> 25996
