<script setup>
const {
    query: { space },
} = useRoute();
const fullscreen_mode = useState("fullscreen_mode", () => false);
const locations = ref([]);
const zoom = ref(12);
const center = ref({ lat: 56.8719851050808, lng: 60.60462041671509 });

const focusedMarker = useState("global_marker", () => {});

const focusOnMarker = (marker) => {
    center.value = {
        lat: marker.parking_latitude,
        lng: marker.parking_longitude,
    };
    zoom.value = 15;
    if (marker.number_of_places <= 0) return
    focusedMarker.value = marker;
};
let gmapOptions = {
    zoomControl: false,
    mapTypeControl: false,
    scaleControl: false,
    streetViewControl: false,
    rotateControl: true,
    fullscreenControl: false,
};

onMounted(async () => {
    setTimeout(async () => {
        const { data, error } = await useAPI("/api/v1/get_places");
        await data
        locations.value = data.value;
        if (space) {
            locations.value.forEach((location) => {
                if (location.id === space) {
                    setTimeout(() => {
                        focusOnMarker(location);
                        fullscreen_mode.value = true;
                    }, 1000);
                }
            });
        }
    }, 1000);
});
</script>
<template>
    <ClientOnly>
        <GMapMap
            @click="focusedMarker = undefined"
            class="map"
            :center="center"
            map-type-id="roadmap"
            :zoom="zoom"
            :options="gmapOptions"
        >
            <GMapCluster :zoomOnClick="true">
                <GMapMarker
                    v-for="(marker, index) in locations"
                    :key="index"
                    :position="{
                        lat: marker.parking_latitude,
                        lng: marker.parking_longitude,
                    }"
                    :clickable="true"
                    :icon="{
                        url: `/images/dot_${marker.number_of_places > 0 ? 'green' : 'red'}.png`,
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
