defmodule ComputePerimeter do
  @doc """
  https://www.hackerrank.com/challenges/lambda-march-compute-the-perimeter-of-a-polygon?
  """
  def distance(x) do
    a = elem(x, 0)
    b = elem(x, 1)

    v = :math.sqrt(
      :math.pow(Enum.at(a, 0) - Enum.at(b, 0), 2) +
      :math.pow(Enum.at(a, 1) - Enum.at(b, 1), 2))
  end

  def solve(points) do
    points = points ++ [hd(points)]
    point_len = length(points)
    pairs = Enum.zip(
      Enum.slice(points, 0..point_len - 1),
      Enum.slice(points, 1..point_len))

    Enum.reduce(
      pairs, 0.0,
      fn (x, acc) ->
        acc + distance(x)
      end)
  end

  def main() do
    n = elem(Integer.parse(IO.gets("")), 0)
    points = for _ <- 1..n do
      IO.gets("")
      |> String.trim()
      |> String.split(" ")
      |> Enum.map(fn (x) -> elem(Integer.parse(x), 0) end)
    end

    IO.puts(solve(points))
  end
end

ComputePerimeter.main()
