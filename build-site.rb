require 'csv'
require 'erb'
require 'date'
require "rqrcode"

# Define the ERB template
template = File.read('template.erb')
erb = ERB.new(template)

# Read and group messages from the CSV file by section
messages_by_section = Hash.new { |hash, key| hash[key] = [] }
folder_ids = {
	"A" => "1krSwRCdWHPKC8hsOzD1nJWHlHNPnm2k6",
	"B" => "1krSwRCdWHPKC8hsOzD1nJWHlHNPnm2k6",
	"C" => "1krSwRCdWHPKC8hsOzD1nJWHlHNPnm2k6",
}
spotify_ids = {
	"A" => "677Cl2ny3YiguR7e0TVxAv",
	"B" => "677Cl2ny3YiguR7e0TVxAv",
	"C" => "677Cl2ny3YiguR7e0TVxAv",
}
CSV.foreach('messages.csv', headers: true) do |row|
  section = row[0].upcase
  name = row[1]
  content = row[2]

  messages_by_section[section] << { name: name, content: content, rot: rand(-5..5) }
end

themes = [["#6BB6C5", "#00596B"], ["#FFBE78" , "#FA8200"], ["#C587FF", "#6700C7"], ["#61FF5B", "#08DD00"], ["#FF5BA5", "#E20066"]]

# Generate an HTML file for each section
messages_by_section.each do |section, messages|
	Dir.mkdir "docs/#{section}"
  File.open("docs/#{section}/index.html", 'w') do |file|
	  theme = themes[rand(0..4)]
    file.write(erb.result(binding))
    qrcode = RQRCode::QRCode.new("https://dips-classof25.github.io/#{section}/index.html")

    # NOTE: showing with default options specified explicitly
    png = qrcode.as_png(
      bit_depth: 1,
      border_modules: 1,
      color_mode: ChunkyPNG::COLOR_GRAYSCALE,
      color: "black",
      file: nil,
      fill: "white",
      module_px_size: 6,
      resize_exactly_to: false,
      resize_gte_to: false,
      size: 512
    )

    IO.binwrite("_codes/#{section}.png", png.to_s)
    puts section
  end
end

puts "HTML files have been generated for each section!"
