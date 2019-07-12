
r = 40075

main = fn () ->
  {n, _} = IO.gets("")
    |> String.trim
    |> Integer.parse

   Kernel.round((2 * :math.pi * n + r) * 10) / 10
   |> IO.puts

end




{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
