const BASE_URL = '/api'

export async function fetchWeather(location) {
  const res = await fetch(`${BASE_URL}/weather?location=${encodeURIComponent(location)}`)
  if (!res.ok) throw new Error('Failed to fetch weather data')
  return res.json()
}
