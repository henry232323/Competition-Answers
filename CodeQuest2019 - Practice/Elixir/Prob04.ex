main = fn () ->
  [a, b] = IO.gets("")
    |> String.trim
    |> String.split(" ")
   bday = b == "true"
   {dspeed, _} = Integer.parse(a)
   speed = cond do
     bday -> dspeed - 5
     true -> dspeed
   end

   cond do
     speed <= 60 ->
       IO.puts("no ticket")
     speed <= 80 ->
       IO.puts("small ticket")
     true ->
       IO.puts("big ticket")
   end
end




{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
