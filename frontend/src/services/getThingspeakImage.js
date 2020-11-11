const thingspeakImageAPI = "https://thingspeak.com/apps/matlab_visualizations";

export default async function getThingspeakImage({ plot_id, width, heigth }) {
  const response = await fetch(
    `${thingspeakImageAPI}/${plot_id}/matlab_display_data.js?height=${heigth}&width=${width}`
  );

  const json = await response.json();

  return json.data_url;
}
