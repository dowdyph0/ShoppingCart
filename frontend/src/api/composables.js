import { ref, computed } from 'vue'
import { LocalStorage } from 'quasar'

const accessRef = ref(LocalStorage.getItem('accessRef'))
const refreshRef = ref(LocalStorage.getItem('refreshRef'))
const access = computed({
    get() {
        if (accessRef.value == '') {
            return null
        }
        return accessRef.value
    },
    set(newVal){
        if (newVal == null || newVal == "") {
            accessRef.value = null
            LocalStorage.remove('accessRef')
        } else {
            accessRef.value = newVal
            LocalStorage.set('accessRef', newVal)
        }
    }
})

const refresh = computed({
    get() {
        if (refreshRef.value == '') {
            return null
        }
        return refreshRef.value
    },
    set(newVal){
        if (newVal == null || newVal == "") {
            refreshRef.value = null
            LocalStorage.remove('refreshRef')
        } else {
            refreshRef.value = newVal
            LocalStorage.set('refreshRef', newVal)
        }
    }
})

export default function projectComposables() {
    return {access, refresh}
}