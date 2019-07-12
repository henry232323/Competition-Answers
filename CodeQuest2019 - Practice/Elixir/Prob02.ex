main = fn () ->
  [{a, _}, {b, _}] = IO.gets("")
    |> String.split(" ")
    |> Enum.map(&Integer.parse/1)

  cond do
    a == b ->
      IO.puts(4 * a)
    true ->
      IO.puts(a + b)
  end
end




{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
