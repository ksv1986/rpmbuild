         DOSBox with pixel-perfect scaling
            and aspect-ratio correction.
                     (alpha 14)

This  patch  adds  several modes of software scaling
based on the 'surface' output type:

surfacepp (pixel-perfect):
   Each emulated pixel is  represented  as  a  sharp
   rectangle  with  integral  dimensions  m x n such
   that m:n approximates the  desired  pixel  aspect
   ratio  (PAR), which depends on the emulated reso-
   lution and the 'aspect' setting in  the  [render]
   section.   Whereas  the  standard  PARs are them-
   selves ratios of small integers, this  mode  will
   yield the exact aspect ratio, provided the output
   resolution is high enough for the game.

surfacenp (near-perfect):
   Upscales the image interpolatively with a minimum
   of  artefacts.   This is similar to supersampling
   with a normaln<x> scaler beyond the display reso-
   lution  and then downscaling to the output dimen-
   sions by bilinear interpolation.  The new parame-
   ter  'surfacenp-sharpness'  in  the [sdl] section
   attenuates the amount  of  interpoation.   It  is
   measured in percent, from 0 to 100, with 100 lat-
   ter corresponding to the nearest-neighbor method.

surfacenb (nearest-neighbor):
   Equivalent to 'openglnb'.

The new value 'desktop'  of  the  'windowresolution'
parameter  causes DOSBox to make the window as large
as the display and scaling method permit.

The  new  parameter  surface-collapse-dbl  specifies
whether to collapse pairs of adjacent pixel rows and
colums in double-height and double-width modes  when
one  of  the new surface-based scalers is in effect.
This is useful, for example, when a double-scan mode
is  emulated but the game does not use it, as is the
case with Lure of the Temptress run with

                [dosbox]
                machine=vgaonly

When the game, however, relies on  double-scan,  en-
abling  collapsing will "serrate" the image by omit-
ting every second pixel row.

The new scaling modes ignore the  built-in  scalers,
enforcing:
                [render]
                scaler=none

With  LCD  displays,  make certain always to use the
native resolution in fullscreen.  To  do  that,  and
assuming  you have configured the correct resolution
in your OS, specify:

                [sdl]
                fullresolution=desktop