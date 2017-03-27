defmodule SumOfOddElements do
  def sum_of_odd(arr) do
    Enum.reduce(
      Enum.filter(arr, fn (x) -> rem(x, 2) == 1 end),
      fn(x, acc) -> x + acc end)
  end

  def input_loop(elements \\ []) do
    case IO.gets("") do
      {:error, _} -> elements
      :eof -> elements
      "\n" -> elements
      data ->
        {element, _} = Integer.parse(data)

        input_loop(elements ++ [element])
    end
  end

  def main() do
    IO.puts(sum_of_odd(input_loop()))
  end
end

SumOfOddElements.main()
