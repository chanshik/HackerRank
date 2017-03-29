defmodule EvaluatingE_X do
  def solve(x) do
    Stream.unfold(0, fn n -> {n, n + 1} end)
    |> Enum.take(10)
    |> Enum.reduce(
      fn (i, acc) ->
        acc + (:math.pow(x, i) / Enum.reduce(1..i, fn (x, acc) -> x * acc end))
      end)
  end

  def main() do
    {n, _} = Integer.parse(IO.gets(""))

    arr = for _ <- 1..n do
      elem(Float.parse(IO.gets("")), 0)
    end

    for x <- arr do
      IO.puts(Float.round(solve(x) + 1, 4))
    end
  end
end

EvaluatingE_X.main()
