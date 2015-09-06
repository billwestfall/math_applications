{-  run as

Prelude> :l page177b.hs
[1 of 1] Compiling Main             ( page177b.hs, interpreted )
Ok, modules loaded: Main.
*Main> costBen 50
16.071428
*Main> costBen 15
2.967033

-}


costBen :: Float -> Float
costBen a = (18 * a) / (106 - a)
