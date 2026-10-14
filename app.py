
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quản Lý Điểm Sinh Viên", layout="centered")

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.markdown("---")

data = {
    'Ho_va_ten': [
        'Nguyễn Văn A', 'Lê Thị B', 'Trần Văn C', 'Phạm Thị D', 'Hoàng Văn E',
        'Đỗ Thị F', 'Vũ Văn G', 'Đặng Thị H', 'Bùi Văn I', 'Ngô Văn K'
    ],
    'Chuyen_can': [9.0, 7.5, 8.0, 6.0, 10.0, 5.0, 8.5, 9.5, 4.0, 7.0],
    'Giua_ky':    [8.0, 6.5, 7.0, 5.5,  9.0, 4.5, 7.5, 8.5, 5.0, 6.0],
    'Cuoi_ky':    [8.5, 7.0, 6.5, 4.0,  9.5, 5.0, 8.0, 9.0, 3.5, 6.5]
}

df = pd.DataFrame(data)
df['Tong_ket'] = (0.20 * df['Chuyen_can'] + 0.30 * df['Giua_ky'] + 0.50 * df['Cuoi_ky']).round(2)

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

st.subheader("📋 Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df, use_container_width=True)

st.subheader("📊 Thống kê chung của lớp")
dtb_lop = df['Tong_ket'].mean()
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Điểm trung bình lớp", value=f"{dtb_lop:.2f}")
    st.metric(label="Số sinh viên đạt (>= 5.0)", value=f"{so_sv_dat} / {len(df)}")

sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]

with col2:
    st.write(f"🏆 **Cao điểm nhất:** {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']} điểm)")
    st.write(f"⚠️ **Thấp điểm nhất:** {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']} điểm)")

st.markdown("---")

st.subheader("🔍 Tra cứu thông tin sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên cần xem:", df['Ho_va_ten'])

student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]

st.info(f"Thông tin chi tiết của: **{selected_student}**")
col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns(5)
col_s1.metric("Chuyên cần", student_info['Chuyen_can'])
col_s2.metric("Giữa kỳ", student_info['Giua_ky'])
col_s3.metric("Cuối kỳ", student_info['Cuoi_ky'])
col_s4.metric("Tổng kết", student_info['Tong_ket'])
col_s5.metric("Xếp loại", student_info['Xep_loai'])

st.markdown("---")

st.subheader("📈 Biểu đồ điểm tổng kết của 10 sinh viên")
chart_data = df.set_index('Ho_va_ten')['Tong_ket']
st.bar_chart(chart_data)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: small; color: gray;'>"
    "Người tạo ứng dụng: ĐỖ VIÊT TÙNG | MSSV: [038208026422]"
    "</p>", 
    unsafe_allow_html=True
)
