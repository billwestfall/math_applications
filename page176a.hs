{-  run as

*Main> :l page176a.hs
[1 of 1] Compiling Main             ( page176a.hs, interpreted )
Ok, modules loaded: Main.
*Main> asymFun 9
4.101266
*Main> asymFun 3
5.142857
*Main> asymFun (-5)
4.347826

-}


asymFun :: Float -> Float
asymFun a = ((2 * a)**2) / (((a)**2) - 2)
