<template>
    <div class="header">
        <h1 class="label">{{label}}</h1>
    </div>
</template>

<script>
    export default {
        props: ['label'],
    }
</script>

<style lang="scss" scoped>
    @font-face{
        font-family: 'Red October';
        src: url('../assets/redoctober.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    .header {
        padding: 4%;
        background-color: #006BDD;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.15);
    }

    .label {
        font-family: 'Red October';
        font-weight: 400;
        font-size: 1.5rem;
        line-height: 2.438rem;
        color: #D9E4F0;
    }
</style>