main = fn () ->
  IO.gets("")
    |> String.downcase
    |> IO.write
end

{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
