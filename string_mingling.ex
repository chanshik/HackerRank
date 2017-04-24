defmodule StringMingling do
  @doc """
  String Mingling
  https://www.hackerrank.com/challenges/string-mingling
  """
  def main() do
    p = IO.gets("")
    q = IO.gets("")

    len_p = String.length(p)

    for idx <- 0..len_p - 1 do
      IO.write(String.at(p, idx))
      IO.write(String.at(q, idx))
    end
  end
end

StringMingling.main()
