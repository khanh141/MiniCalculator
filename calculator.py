import streamlit as st

st.title("Mini Calculator!")

# khởi tạo bộ nhớ
if 'expression' not in st.session_state:
    st.session_state.expression = ""
    
if 'just_calculated' not in st.session_state:
    st.session_state.just_calculated = False
    
# hàm nhập 
def button_click(value):
    operator_map = {
        "➕": "+",
        "➖": "-",
        "✖️": "*",
        "➗": "/"
    }
    
    operators = operator_map.values()
    
# xử lý sau khi đã tính toán xong, nếu người dùng nhập tiếp một phép toán thì sẽ tiếp tục tính
    if st.session_state.just_calculated:
        if value in operators:
            st.session_state.just_calculated = False
        else:
            st.session_state.expression = ""
            st.session_state.just_calculated = False


# xử lý phần thập phân
    if value == ".":
        parts = st.session_state.expression.split("+")
        parts = parts[-1].split("-")
        parts = parts[-1].split("*")
        parts = parts[-1].split("/")

        current_number = parts[-1]
    
        if "." in current_number:
            return
        
    
    if value in operator_map:
        op = operator_map[value]
        # kiểm tra  nếu biểu thưc bắt đầu bằng phép tính + x /
        if st.session_state.expression == "" and op in ["+", "*", "/"]:
            return  
        # kiểm tra nếu biểu thức đang kết thúc bằng phép tính mà bấm tiếp phép tính sẽ thực hiện thay thế 
        if st.session_state.expression[-1] in operators:
            # st.session_state.expression[:-1] lấy tất cả kí tự trừ kí tự cuối cùng
            st.session_state.expression = (st.session_state.expression[:-1] + op) 
        else:
            st.session_state.expression += op
    else:
        st.session_state.expression += str(value)
    
# hàm tính toán
def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
        st.session_state.just_calculated = True
    except:
        st.session_state.expression = "Error"
        
# hàm xoá màn hình 
def clear():
    st.session_state.expression = ""
    st.session_state.just_calculated = False
# hiển thị
st.text_input("",key="expression",disabled=True)

# khởi tạo nút
buttons = [
    ["7", "8", "9", "➗"],
    ["4", "5", "6", "✖️"],
    ["1", "2", "3", "➖"],
    ["0", ".", "C", "➕"],
]

st.markdown("""
<style>
div.stButton > button {
    height: 40px;
    font-size: 26px;
    font-weight: bold;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

for row in buttons:
    cols = st.columns(4)
    for i, label in enumerate(row):
        if label == "C":
            cols[i].button(label,use_container_width=True, on_click=clear)
        else:
            cols[i].button(label,use_container_width=True, on_click=button_click, args=(label,))
            
# kết quả     
cols = st.columns(4)
cols[0].button("=",use_container_width=True, on_click=calculate)
cols[1].empty()
cols[2].empty()
cols[3].empty()