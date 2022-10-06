import { ref, computed } from 'vue'
import { LocalStorage } from 'quasar'
import jwt_decode from "jwt-decode";

const accessRef = ref(LocalStorage.getItem('accessRef'))
const refreshRef = ref(LocalStorage.getItem('refreshRef'))

const access = computed({
    get() {
        if (accessRef.value == '') {
            return null
        }
        return accessRef.value
    },
    set(newVal) {
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
    set(newVal) {
        if (newVal == null || newVal == "") {
            refreshRef.value = null
            LocalStorage.remove('refreshRef')
        } else {
            refreshRef.value = newVal
            LocalStorage.set('refreshRef', newVal)
        }
    }
})

const getCartID = () => {
    if (accessRef.value != null) {
        try {
            var decoded_jwt = jwt_decode(accessRef.value)
            return decoded_jwt.cart_id
        } catch {
            return null
        }
    }
}

const isSuperUser = () => {
    if (accessRef.value != null) {
        try {
            var decoded_jwt = jwt_decode(accessRef.value)
            return decoded_jwt.is_superuser
        } catch {
        }
    }
    return false
}

export default function projectComposables() {
    return { access, refresh, getCartID, isSuperUser }
}