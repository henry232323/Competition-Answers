main = fn () ->
  [a, b] = IO.gets("")
    |> String.trim
    |> String.split(" ")
    |> Enum.map(fn (x) -> x == "true" end)

  cond do
    a == b ->
      IO.puts("true")
    true ->
      IO.puts("false")
  end
end




{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
