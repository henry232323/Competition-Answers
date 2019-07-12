main = fn () ->
  {n, _} = IO.gets("")
    |> String.trim
    |> Integer.parse

    numbers = for _ <- 1..n do
      {n, _} = IO.gets("")
        |> String.trim
        |> Float.parse
      n
    end
    {min, max} = Enum.min_max(numbers)
    for k <- numbers do
      (k-min)/(max-min) * 255
      |> Kernel.round
      |> IO.puts
    end

end




{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
