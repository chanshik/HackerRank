defmodule UpdateList do
  def solve(arr) do
    for item <- Enum.map(arr, fn (x) -> abs(x) end) do
      IO.puts(item)
    end
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

UpdateList.main()
