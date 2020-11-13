import React, { useCallback, useEffect, useState } from "react";
import Image, { Shimmer } from "react-shimmer";
import { MdRefresh } from "react-icons/md";

import "./styles.css";

import getThingspeakImage from "../../services/getThingspeakImage";

function ThingSpeakChart({
  plot_id,
  heigth = 260,
  width = 450,
  refresh = true,
}) {
  const [imageUrl, setImageUrl] = useState("");

  const loadThingspeakImage = useCallback(async () => {
    const thingspeakImageUrl = await getThingspeakImage({
      plot_id,
      width,
      heigth,
    });
    setImageUrl(thingspeakImageUrl);
  }, [plot_id, heigth, width]);

  useEffect(() => {
    loadThingspeakImage();
  }, [loadThingspeakImage]);

  if (!imageUrl) {
    return <Shimmer width={width} height={heigth} />;
  }

  return (
    <div id="thingspeak-chart">
      {refresh && (
        <div
          className="refresh"
          onClick={() => {
            setImageUrl("");
            loadThingspeakImage();
          }}
        >
          <MdRefresh size={20} />
          <span>Recarregar gráfico</span>
        </div>
      )}

      {imageUrl && (
        <Image
          src={imageUrl}
          alt={plot_id}
          fallback={<Shimmer width={width} height={heigth} />}
        />
      )}
      {!imageUrl && <Shimmer width={width} height={heigth} />}
    </div>
  );
}

export default ThingSpeakChart;
