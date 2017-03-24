defmodule FilterArray do
  @moduledoc false
  def filter_array(_, []) do
    :ok
  end

  def filter_array(x, arr) do
    [head | tail] = arr
    if head < x do
      IO.puts(head)
    end

    filter_array(x, tail)
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
    {x, _} = Integer.parse(IO.gets(""))

    filter_array(x, input_loop([]))
  end
end

FilterArray.main()