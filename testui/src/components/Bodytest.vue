<template>
    <div 
        v-if="!quizComplited"
    >
        <div class="question">
            <p class="text">{{ getCurrentQuestion.question }}</p>
        </div>
        <div class="options">
            <label 
                class="answer"
                v-for="(option, index) in getCurrentQuestion.options"
                :for="'option' + index"
                :class="`option ${
                    getCurrentQuestion.selected == index
                        ? index == getCurrentQuestion.answer
                            ? 'correct'
                            : 'wrong'
                        : ''
                } ${
                    getCurrentQuestion.selected != null &&
                    index != getCurrentQuestion.selected
                        ? 'disabled'
                        : ''
                }`"
                >
                <input 
                    type="radio"
                    :id="'option' + index"
                    :name="getCurrentQuestion.index"
                    :value="index"
                    v-model="getCurrentQuestion.selected"
                    :disabled="getCurrentQuestion.selected"
                    @change="SetAnswer"
                    style="display: none;"
                >
                <p class="text">
                    {{ option }}
                </p>
            </label>
        </div>
        <div 
            class="next"
            @click="NextQuestion"
            :disabled="!getCurrentQuestion.selected"
        >
            <h1 class="text">
            {{
                getCurrentQuestion.index == questions.length - 1
                    ? 'Закончить'
                    : getCurrentQuestion.selected == null
                        ? 'Выберите'
                        : 'Далее'
            }}
            </h1>
        </div>
    </div>
    <div 
        class="question"
        v-else
    >
        <p class="text">
            Спасибо за прохождение теста! <br>
            Ваш результат: {{ score }} / {{ questions.length }}
        </p>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const questions = ref([
    {
        question: 'Венчание на царство Ивана IV состоялось',
        answer: 2,
        options: [
            '16 января 1533г.',
            '16 января 1537г.',
            '16 января 1547г.',
            '16 января 1578г.'
        ],
        selected: null
    },
    {
        question: 'Современниками Ивана Грозного были',
        answer: 0,
        options: [
            'Елена Глинская, митрополит Макарий',
            'Борис Годунов, патриарх Филарет',
            'протопоп Аввакум, патриарх Никон',
            'хан Батый, литовский князь Миндовг'
        ],
        selected: null
    },
    {
        question: 'Войско, созданное в правление Ивана Грозного',
        answer: 0,
        options: [
            'стрелецкое',
            'рекрутское',
            'драгунское',
            'гусарское'
        ],
        selected: null
    },
    {
        question: 'Реформация XVI в. началась в (во)',
        answer: 1,
        options: [
            'Швейцарии',
            'Германии',
            'Франции',
            'Италии'
        ],
        selected: null
    },
    {
        question: 'Монархия во Франции была свергнута в: ',
        answer: 2,
        options: [
            '1790 г.',
            '1791 г.',
            '1792 г.',
            '1793 г.'
        ],
        selected: null
    },
    {
        question: 'Кто первым разработал принцип разделения властей?',
        answer: 2,
        options: [
            'Джон Кей',
            'Джеймс Уатт',
            'Монтескье',
            'Джон Локк'
        ],
        selected: null
    },
    {
        question: 'Выберите имя просветителя',
        answer: 1,
        options: [
            'Марат',
            'Вольтер',
            'Гиз',
            'Дрейк'
        ],
        selected: null
    },
    {
        question: 'Первым крупным тайным обществом декабристов стал',
        answer: 3,
        options: [
            '«Союз благоденствия»',
            '«Союз офицеров»',
            '«Союз ради прогресса»',
            '«Союз спасения»'
        ],
        selected: null
    },
])

const quizComplited = ref(false)
const currentQuestion = ref(0)
const score = computed(() => {
    let value = 0
    questions.value.map(q => {
        if(q.selected == q.answer) {
            value++
        }
    })
    return value
})

const getCurrentQuestion = computed(() => {
    let question = questions.value[currentQuestion.value]
    question.index = currentQuestion.value
    return question
})

const SetAnswer = (e) => {
    questions.value[currentQuestion.value].selected = e.target.value
    e.target.value = null
}

const NextQuestion = () => {
    if(currentQuestion.value < questions.value.length - 1) {
        currentQuestion.value++
    }
    else {
        quizComplited.value = true
    }
}

</script>

<style lang="scss" scoped>
    .question {
        margin: 5%;
        margin-bottom: 15%;
        padding: 5%;
        background: rgba(217, 217, 217, 0.6);
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.15);
        border-radius: 25rem;

        text-align: center;

        .text {
            font-family: 'Red October';
            font-style: normal;
            font-weight: 400;
            font-size: 1.2rem;
            line-height: 1.8rem;
            color: #3a38cc;
        }
    }
    
    .answer {
        display: block;
        margin: 5%;
        padding: 5%;
        background: rgba(217, 217, 217, 0.6);
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.15);
        border-radius: 25rem;

        text-align: center;

        .text {
            font-family: 'Red October';
            font-style: normal;
            font-weight: 400;
            font-size: 1rem;
            line-height: 2rem;
            color: #3a38cc;
        }

    }

    .answer.correct {
        background-color: rgba(40, 255, 88, 0.6);
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.15);
    }

    .answer.wrong {
        background-color: rgba(255, 28, 28, 0.6);
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.15);
    }

    .next {
        margin: 10% 25%;
        padding: 5%;
        background: rgba(0, 107, 221, 0.6);
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.15);
        border-radius: 25rem;

        text-align: center;

        .text {
            font-family: 'Red October';
            font-style: normal;
            font-weight: 400;
            font-size: 1.5rem;
            line-height: 1.5rem;
            color: rgba(217, 217, 217, 0.9);
        }
    }
</style>