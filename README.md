# opsdroid skill taginfo

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to get openstreetmap data from taginfo e.g. https://taginfo.openstreetmap.org/


## Usage

#### `!tg highway=steps`
#### `!tg highway=*`
#### `!tg school`

> user: you check check steps like this !tg highway=steps

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

> user: or all highway values !tg highway=*

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


> user: !tg school

> opsdroid: 
> 
>           ### Occurence of value school ###
>           amenity = school - 4232
>           building = school - 2890
>           amenity = driving_school - 63
>           building:part = school - 52
>           amenity = music_school - 28
>           operator:type = school - 18
>           amenity = language_school - 15
>           amenity = ski_school - 13
>           abandoned:amenity = school - 7
>           animal = school - 6
