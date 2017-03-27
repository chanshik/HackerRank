defmodule ListLength do
  def solve(arr) do
    IO.puts(Enum.reduce(arr, 0, fn(_, acc) -> 1 + acc end))
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
    solve(input_loop())
  end
end

ListLength.main()
