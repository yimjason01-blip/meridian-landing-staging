# Figma Layer Manifest

## Coordinate system

All bounding boxes are frame relative pixels in the 1728 x 968 hero frame or 1728 x 861 curve frame. DOM positions are converted to percentages from these boxes.

## Hero stable UI

- All slides | 674:41500 | Logo | FRAME | x 72, y 48, w 128, h 32 | logo_4x.png | .brand-logo | stable UI | z 50 | none | real image DOM
- All slides | 674:41514 | Your best days are still ahead. | TEXT | x 72, y 675, w 537, h 130 | none | .headline | stable UI | z 50 | none | real text DOM
- All slides | 674:41754 | Apply Button | INSTANCE | x 1554, y 34, w 137, h 59 | none | .figma-button.apply | stable UI | z 60 | none | real anchor DOM
- All slides | 674:41513 | Demo Button | INSTANCE | x 72, y 845, w 140, h 61 | none | .figma-button.demo | stable UI | z 60 | none | real anchor DOM
- All slides | 674:41516 | Current count | TEXT | x 867, y 865, w 26, h 14 | none | .slide-count.current | stable UI | z 50 | none | real text DOM
- All slides | 674:41515 | Total count | TEXT | x 1536, y 865, w 35, h 14 | none | .slide-count.total | stable UI | z 50 | none | real text DOM
- All slides | derived | Carousel dots | CONTROL | center bottom | none | .carousel-dot | stable UI | z 70 | none | real button DOM

## Hero slide 1

- Slide 1 | 674:41457 | ChatGPT background photo | RECTANGLE | x 0, y 4, w 2470, h 1591 | photo_base_41457.png | .slide-one .photo-base-bg | photo background | z 10 | carousel | Figma image crop
- Slide 1 | 674:41458 | Natalia background photo | RECTANGLE | x 202, y 0, w 1539, h 968 | natalia_41458.png | .slide-one .photo-natalia-bg | photo background | z 11 | carousel | Figma image crop
- Slide 1 | 674:41459 | Lawrence photo | RECTANGLE | x 224, y -687, w 1506, h 2258 | lawrence_41459.png | .slide-one .photo-primary | photo primary | z 12 | carousel | Figma image crop
- Slide 1 | 674:41460 | Union | BOOLEAN_OPERATION | x 0, y 3.6, w 1728, h 968.4 | base_union_41460_static.png | .slide-one .base-union | anchored color mass | z 20 | none | static raster with moving block removed
- Slide 1 | 674:41466 | Grid Gradient | FRAME | x 0, y 0, w 1733.4, h 972 | grid_gradient_41466_static.png | .slide-one .grid-gradient-back | anchored grid back | z 30 | none | static raster with moving block removed
- Slide 1 | 674:41474 | Rectangle 158 | RECTANGLE | x 740, y 487, w 243, h 121.05 | slide1_block_mid_41474.png | .slide-one .floating-block.between-faces | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 1 | 674:41462, 674:41477, 674:41494 | Rectangle 151 stack | RECTANGLE | x 515.7, y 608, w 224, h 121 | slide1_block_lower_41462_41477_41494.png | .slide-one .floating-block.lower-left | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 1 | 674:41497 | Rectangle 155 | RECTANGLE | x 1485, y 607.95, w 243, h 121.05 | slide1_block_right_41497.png | .slide-one .floating-block.far-right | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 1 | 674:41485 | Lawrence foreground | RECTANGLE | x 224, y -687, w 1506, h 2258 | subject_cutout_41459_expanded.png | .slide-one .photo-foreground | foreground subject | z 40 | carousel | derived alpha cutout
- Slide 1 | 674:41486 | Grid Gradient front | FRAME | x 0, y 0, w 1733.4, h 972 | fg_grid_gradient_41486_static.png | .slide-one .grid-gradient-front | anchored grid front | z 45 | none | static raster with moving block removed

## Hero slide 2

- Slide 2 | 674:41871 | Kirsten photo | RECTANGLE | x 271, y -902, w 1457, h 2185 | slide2_photo_41871.png | .slide-two .photo-primary | photo primary | z 12 | carousel | Figma image crop
- Slide 2 | 674:41872 | Grid Gradient back | FRAME | x 0, y 0, w 1733.4, h 972 | slide2_blocks_back_41872_static.png | .slide-two .grid-gradient-back | anchored grid back | z 30 | none | static raster
- Slide 2 | 674:41880 | Rectangle 158 | RECTANGLE | x 740, y 487, w 243, h 121.05 | slide2_block_mid_41880.png | .slide-two .floating-block.between-faces | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 2 | 674:41884 | Rectangle 155 | RECTANGLE | x 1485, y 607.95, w 243, h 121.05 | slide2_block_right_41884.png | .slide-two .floating-block.far-right | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 2 | 674:41891 | Grid Gradient front | FRAME | x 0, y 0, w 1733.4, h 972 | slide2_blocks_front_41891_static.png | .slide-two .grid-gradient-front | anchored grid front | z 45 | none | static raster
- Slide 2 | 674:41904 | Kirsten foreground | RECTANGLE | x 271, y -901, w 1457, h 2185 | slide2_photo_fg_41904.png | .slide-two .photo-foreground | foreground subject | z 40 | carousel | Figma image crop

## Hero slide 3

- Slide 3 | 674:42199 | Getty photo | RECTANGLE | x 265, y -86, w 1582, h 1054 | slide3_photo_42199.png | .slide-three .photo-primary | photo primary | z 12 | carousel | Figma image crop
- Slide 3 | 674:42200 | Union | BOOLEAN_OPERATION | x 0, y 3.6, w 1728, h 968.4 | slide3_base_union_42200_static.png | .slide-three .base-union | anchored color mass | z 20 | none | static raster
- Slide 3 | 674:42206 | Grid Gradient back | FRAME | x 0, y 0, w 1733.4, h 972 | slide3_blocks_back_42206_static.png | .slide-three .grid-gradient-back | anchored grid back | z 30 | none | static raster
- Slide 3 | 674:42203 | Rectangle 155 | RECTANGLE | x 1483, y 609, w 245, h 121 | slide3_block_right_42203.png | .slide-three .floating-block.far-right | floating block | z 25 | carousel and parallax | independent DOM image behind foreground
- Slide 3 | 674:42214 | Rectangle 158 | RECTANGLE | x 740, y 487, w 243, h 121.05 | slide3_block_mid_42214.png | .slide-three .floating-block.between-faces | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 3 | 674:42225 | Getty foreground | RECTANGLE | x 265, y -86, w 1582, h 1054 | slide3_photo_fg_42225.png | .slide-three .photo-foreground | foreground subject | z 40 | carousel | Figma image crop
- Slide 3 | 674:42226 | Grid Gradient front | FRAME | x 0, y 0, w 1733.4, h 972 | slide3_blocks_front_42226_static.png | .slide-three .grid-gradient-front | anchored grid front | z 45 | none | static raster

## Hero slide 4

- Slide 4 | 674:43053 | ChatGPT background photo | RECTANGLE | x 0, y 4, w 2470, h 1591 | slide4_base_photo_43053.png | .slide-four .photo-base-full | photo background | z 10 | carousel | Figma image crop
- Slide 4 | 674:43082 | Union | BOOLEAN_OPERATION | x 0, y 3.6, w 1728, h 968.4 | slide4_base_union_43082_static.png | .slide-four .base-union | anchored color mass | z 20 | none | static raster
- Slide 4 | 674:43088 | Getty photo | RECTANGLE | x 265, y -269, w 2087, h 1392 | slide4_photo_43088.png | .slide-four .photo-primary | photo primary | z 12 | carousel | Figma image crop
- Slide 4 | 674:43089 | Grid Gradient back | FRAME | x 0, y 0, w 1733.4, h 972 | slide4_blocks_back_43089_static.png | .slide-four .grid-gradient-back | anchored grid back | z 30 | none | static raster
- Slide 4 | 674:43097 | Rectangle 158 | RECTANGLE | x 740, y 487, w 243, h 121.05 | slide4_block_mid_43097.png | .slide-four .floating-block.between-faces | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 4 | 674:43101 | Rectangle 155 | RECTANGLE | x 1485, y 607.95, w 243, h 121.05 | slide4_block_right_43101.png | .slide-four .floating-block.far-right | floating block | z 35 | carousel and parallax | independent DOM image
- Slide 4 | 693:43384 | Getty foreground | RECTANGLE | x 264, y -269, w 2087, h 1392 | slide4_photo_fg_69343384.png | .slide-four .photo-foreground | foreground subject | z 40 | carousel | Figma image crop
- Slide 4 | 674:43109 | Grid Gradient front | FRAME | x 0, y 0, w 1733.4, h 972 | slide4_blocks_front_43109_static.png | .slide-four .grid-gradient-front | anchored grid front | z 45 | none | static raster

## Curve section

- Curve | 674:41521 | Frame 91 | FRAME | x 0, y 0, w 1728, h 737 | section2_bg_grid.png | .curve-bg-grid | static art | z 10 | none | raster grid
- Curve | 674:41538 | Chart | GROUP | x 248, y 247, w 1235, h 489 | section2_chart.png | .curve-line | static art | z 20 | none | raster chart
- Curve | 674:41545 | The story of your future is written on top of this curve. | TEXT | x 517, y 68, w 694, h 101 | none | .curve-title | stable UI | z 30 | none | real text DOM
- Curve | 674:41546 | Play Video button | INSTANCE | x 780, y 216, w 172, h 59 | none | .play-video | stable UI | z 40 | none | real anchor DOM
- Curve | 674:41564 | Age 40 card | GROUP | x 201, y 304, w 91, h 105.38 | none | .age-card.left | DOM card | z 50 | none | real DOM
- Curve | 674:41547 | Age 90 card | GROUP | x 1436, y 574, w 91, h 105.38 | none | .age-card.right | DOM card | z 50 | none | real DOM
- Curve | 674:41562 | Start marker | RECTANGLE | x 239, y 422, w 17, h 17 | none | .curve-marker.start | DOM marker | z 50 | none | real DOM
- Curve | 674:41563 | End marker | RECTANGLE | x 1474, y 693, w 17, h 17 | none | .curve-marker.end | DOM marker | z 50 | none | real DOM
- Curve | 674:41559 to 674:41561 | Axis labels | TEXT | y 757 | none | .axis-label | stable UI | z 50 | none | real text DOM
