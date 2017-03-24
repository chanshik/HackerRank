defmodule FilterPosition do
  @moduledoc false
  def filter_position([], _), do: :ok

  def filter_position(arr, idx) do
    [head | tail] = arr

    if rem(idx, 2) != 0, do: IO.puts(head)

    filter_position(tail, idx + 1)
  end

  def input_loop(elements \\ []) do
    case IO.gets("") do
      :eof -> elements
      "\n" -> elements
      data ->
        {element, _} = Integer.parse(data)

        input_loop(elements ++ [element])
    end
  end

  def main() do
    filter_position(input_loop(), 0)
  end
end

FilterPosition.main()