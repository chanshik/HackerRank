defmodule Curve do
  @doc """
  Area Under Curves and Volume of Revolving a Curve
  https://www.hackerrank.com/challenges/area-under-curves-and-volume-of-revolving-a-curv
  """
  def f(x, arr_a, arr_b) do
    Enum.zip(arr_a, arr_b)
    |> Enum.reduce(0.0,
      fn (iter, acc) ->
        a = elem(iter, 0); b = elem(iter, 1);
        acc + a * :math.pow(x, b) end)
  end

  def area(x_a, x_b, arr_a, arr_b) do
    value = x_a * 1000..x_b * 1000
    |> Enum.map(fn (x) -> f(x * 0.001, arr_a, arr_b) end)
    |> Enum.reduce(0.0, fn (x, acc) -> x + acc end)

    Float.round(value / 1000.0, 1)
  end

  def volume(x_a, x_b, arr_a, arr_b) do
    value = x_a * 1000..x_b * 1000
    |> Enum.map(fn (x) -> f(x * 0.001, arr_a, arr_b) end)
    |> Enum.reduce(0.0, fn (x, acc) -> :math.pi * x * x + acc end)

    Float.round(value / 1000.0, 1)
  end

  def input_arr() do
    IO.gets("")
    |> String.trim()
    |> String.split(" ")
    |> Enum.map(fn (x) -> elem(Integer.parse(x), 0) end)
  end
  def main() do
    arr_a = input_arr()
    arr_b = input_arr()
    [x_a, x_b] = input_arr()

    area(x_a, x_b, arr_a, arr_b)
    |> IO.puts()

    volume(x_a, x_b, arr_a, arr_b)
    |> IO.puts()
  end
end

Curve.main()
