<script setup>
const locations = ref([
    {
        id: 1,
        position: {
            lat: 56.84309925140014,
            lng: 60.645409215528794,
        },
        positionName: "",
    },
    {
        id: 2,
        position: {
            lat: 56.874319783873304,
            lng: 60.539462099983076,
        },
    },
    {
        id: 3,
        position: {
            lat: 56.874319783873305,
            lng: 60.530462099984071,
        },
    },
]);
const zoom = ref(12);
const center = ref({ lat: 56.8719851050808, lng: 60.60462041671509 });

const focusedMarker = useState("global_marker", () => {})

const focusOnMarker = (marker) => {
    center.value = marker.position;
    zoom.value = 15;
    focusedMarker.value = marker
};
let gmapOptions = {
  zoomControl: false,
  mapTypeControl: false,
  scaleControl: false,
  streetViewControl: false,
  rotateControl: true,
  fullscreenControl: false,
}

</script>
<template>
    <ClientOnly>
        <GMapMap
            class="map"
            :center="center"
            map-type-id="roadmap"
            :zoom="zoom"
            :options="gmapOptions">
            <GMapCluster :zoomOnClick="true">
                <GMapMarker
                    v-for="(marker, index) in locations"
                    :key="index"
                    :position="marker.position"
                    :clickable="true"
                    :icon="{
                        url: `/images/dot_green.png`, // There is also dot_grey.png for unknown and dot_red.png for occupied spaces
                        scaledSize: { width: 20, height: 20 },
                        labelOrigin: { x: 16, y: 0 },
                    }"
                    @click="focusOnMarker(marker)"
                />
            </GMapCluster>
        </GMapMap>
    </ClientOnly>
</template>

<style scoped>
.map {
    position: relative;
    height: 100vh;
}
</style>
