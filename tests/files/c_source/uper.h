/**
 * The MIT License (MIT)
 *
 * Copyright (c) 2018 Erik Moqvist
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use, copy,
 * modify, merge, publish, distribute, sublicense, and/or sell copies
 * of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 * BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 * ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

/**
 * This file was generated by asn1tools version 0.138.2 Mon Dec 31 18:44:43 2018.
 */

#ifndef UPER_H
#define UPER_H

#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>

#ifndef ENOMEM
#    define ENOMEM 12
#endif

#ifndef EINVAL
#    define EINVAL 22
#endif

#ifndef EOUTOFDATA
#    define EOUTOFDATA 500
#endif

#ifndef EBADCHOICE
#    define EBADCHOICE 501
#endif

#ifndef EBADLENGTH
#    define EBADLENGTH 502
#endif

/**
 * Type A in module CSource.
 */
struct uper_c_source_a_t {
    int8_t a;
    int16_t b;
    int32_t c;
    int64_t d;
    uint8_t e;
    uint16_t f;
    uint32_t g;
    uint64_t h;
    bool k;
    struct {
        uint8_t buf[11];
    } l;
};

/**
 * Type B in module CSource.
 */
enum uper_c_source_b_choice_e {
    uper_c_source_b_choice_a_e,
    uper_c_source_b_choice_b_e,
    uper_c_source_b_choice_c_e
};

struct uper_c_source_b_t {
    enum uper_c_source_b_choice_e choice;
    union {
        int8_t a;
        struct uper_c_source_a_t b;
    } value;
};

/**
 * Type C in module CSource.
 */
struct uper_c_source_c_t {
    uint8_t length;
    struct uper_c_source_b_t elements[2];
};

/**
 * Type D in module CSource.
 */
enum uper_c_source_d_a_b_choice_e {
    uper_c_source_d_a_b_choice_c_e,
    uper_c_source_d_a_b_choice_d_e
};

enum uper_c_source_d_g_h_e {
    uper_c_source_d_g_h_i_e,
    uper_c_source_d_g_h_j_e,
    uper_c_source_d_g_h_k_e
};

struct uper_c_source_d_t {
    uint8_t length;
    struct {
        struct {
            struct {
                enum uper_c_source_d_a_b_choice_e choice;
                union {
                    uint8_t c;
                    bool d;
                } value;
            } b;
            struct {
                uint8_t length;
            } e;
        } a;
        struct {
            enum uper_c_source_d_g_h_e h;
            struct {
                uint8_t length;
                uint8_t buf[2];
            } l;
        } g;
        struct {
            bool is_n_present;
            bool n;
            int8_t o;
            bool is_p_present;
            struct {
                struct {
                    uint8_t buf[5];
                } q;
                bool is_r_present;
                bool r;
            } p;
        } m;
    } elements[10];
};

/**
 * Type E in module CSource.
 */
enum uper_c_source_e_a_b_choice_e {
    uper_c_source_e_a_b_choice_c_e
};

enum uper_c_source_e_a_choice_e {
    uper_c_source_e_a_choice_b_e
};

struct uper_c_source_e_t {
    struct {
        enum uper_c_source_e_a_choice_e choice;
        union {
            struct {
                enum uper_c_source_e_a_b_choice_e choice;
                union {
                    bool c;
                } value;
            } b;
        } value;
    } a;
};

/**
 * Type F in module CSource.
 */
struct uper_c_source_f_t {
    uint8_t length;
    struct {
        bool elements[1];
    } elements[2];
};

/**
 * Type G in module CSource.
 */
struct uper_c_source_g_t {
    bool is_a_present;
    bool a;
    bool is_b_present;
    bool b;
    bool is_c_present;
    bool c;
    bool is_d_present;
    bool d;
    bool is_e_present;
    bool e;
    bool is_f_present;
    bool f;
    bool is_g_present;
    bool g;
    bool is_h_present;
    bool h;
    bool is_i_present;
    bool i;
};

/**
 * Type H in module CSource.
 */
struct uper_c_source_h_t {
    uint8_t dummy;
};

/**
 * Type I in module CSource.
 */
struct uper_c_source_i_t {
    uint8_t buf[24];
};

/**
 * Type J in module CSource.
 */
struct uper_c_source_j_t {
    uint8_t length;
    uint8_t buf[23];
};

/**
 * Type K in module CSource.
 */
enum uper_c_source_k_e {
    uper_c_source_k_a_e
};

struct uper_c_source_k_t {
    enum uper_c_source_k_e value;
};

/**
 * Type L in module CSource.
 */
struct uper_c_source_l_t {
    uint32_t length;
    uint8_t buf[500];
};

/**
 * Type O in module CSource.
 */
struct uper_c_source_o_t {
    uint32_t length;
    bool elements[260];
};

/**
 * Type N in module CSource.
 */
struct uper_c_source_n_t {
    struct uper_c_source_k_t a;
    struct uper_c_source_a_t b;
    struct uper_c_source_o_t c;
};

/**
 * Type M in module CSource.
 */
struct uper_c_source_m_t {
    struct uper_c_source_k_t a;
    struct uper_c_source_n_t b;
};

/**
 * Type P in module CSource.
 */
struct uper_c_source_p_t {
    struct uper_c_source_a_t a;
    struct uper_c_source_m_t b;
    struct uper_c_source_f_t c;
};

/**
 * Type Bool in module ProgrammingTypes.
 */
struct uper_programming_types_bool_t {
    bool value;
};

/**
 * Type Double in module ProgrammingTypes.
 */
struct uper_programming_types_double_t {
    uint8_t dummy;
};

/**
 * Type Float in module ProgrammingTypes.
 */
struct uper_programming_types_float_t {
    uint8_t dummy;
};

/**
 * Type Int16 in module ProgrammingTypes.
 */
struct uper_programming_types_int16_t {
    int16_t value;
};

/**
 * Type Int32 in module ProgrammingTypes.
 */
struct uper_programming_types_int32_t {
    int32_t value;
};

/**
 * Type Int64 in module ProgrammingTypes.
 */
struct uper_programming_types_int64_t {
    int64_t value;
};

/**
 * Type Int8 in module ProgrammingTypes.
 */
struct uper_programming_types_int8_t {
    int8_t value;
};

/**
 * Type Uint16 in module ProgrammingTypes.
 */
struct uper_programming_types_uint16_t {
    uint16_t value;
};

/**
 * Type Uint32 in module ProgrammingTypes.
 */
struct uper_programming_types_uint32_t {
    uint32_t value;
};

/**
 * Type Uint64 in module ProgrammingTypes.
 */
struct uper_programming_types_uint64_t {
    uint64_t value;
};

/**
 * Type Uint8 in module ProgrammingTypes.
 */
struct uper_programming_types_uint8_t {
    uint8_t value;
};

/**
 * Encode type A defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_a_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_a_t *src_p);

/**
 * Decode type A defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_a_decode(
    struct uper_c_source_a_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type B defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_b_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_b_t *src_p);

/**
 * Decode type B defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_b_decode(
    struct uper_c_source_b_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type C defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_c_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_c_t *src_p);

/**
 * Decode type C defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_c_decode(
    struct uper_c_source_c_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type D defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_d_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_d_t *src_p);

/**
 * Decode type D defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_d_decode(
    struct uper_c_source_d_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type E defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_e_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_e_t *src_p);

/**
 * Decode type E defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_e_decode(
    struct uper_c_source_e_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type F defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_f_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_f_t *src_p);

/**
 * Decode type F defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_f_decode(
    struct uper_c_source_f_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type G defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_g_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_g_t *src_p);

/**
 * Decode type G defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_g_decode(
    struct uper_c_source_g_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type H defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_h_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_h_t *src_p);

/**
 * Decode type H defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_h_decode(
    struct uper_c_source_h_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type I defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_i_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_i_t *src_p);

/**
 * Decode type I defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_i_decode(
    struct uper_c_source_i_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type J defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_j_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_j_t *src_p);

/**
 * Decode type J defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_j_decode(
    struct uper_c_source_j_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type K defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_k_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_k_t *src_p);

/**
 * Decode type K defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_k_decode(
    struct uper_c_source_k_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type L defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_l_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_l_t *src_p);

/**
 * Decode type L defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_l_decode(
    struct uper_c_source_l_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type O defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_o_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_o_t *src_p);

/**
 * Decode type O defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_o_decode(
    struct uper_c_source_o_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type N defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_n_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_n_t *src_p);

/**
 * Decode type N defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_n_decode(
    struct uper_c_source_n_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type M defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_m_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_m_t *src_p);

/**
 * Decode type M defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_m_decode(
    struct uper_c_source_m_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type P defined in module CSource.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_c_source_p_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_c_source_p_t *src_p);

/**
 * Decode type P defined in module CSource.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_c_source_p_decode(
    struct uper_c_source_p_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Bool defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_bool_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_bool_t *src_p);

/**
 * Decode type Bool defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_bool_decode(
    struct uper_programming_types_bool_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Double defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_double_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_double_t *src_p);

/**
 * Decode type Double defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_double_decode(
    struct uper_programming_types_double_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Float defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_float_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_float_t *src_p);

/**
 * Decode type Float defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_float_decode(
    struct uper_programming_types_float_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Int16 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_int16_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_int16_t *src_p);

/**
 * Decode type Int16 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_int16_decode(
    struct uper_programming_types_int16_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Int32 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_int32_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_int32_t *src_p);

/**
 * Decode type Int32 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_int32_decode(
    struct uper_programming_types_int32_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Int64 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_int64_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_int64_t *src_p);

/**
 * Decode type Int64 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_int64_decode(
    struct uper_programming_types_int64_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Int8 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_int8_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_int8_t *src_p);

/**
 * Decode type Int8 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_int8_decode(
    struct uper_programming_types_int8_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Uint16 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_uint16_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_uint16_t *src_p);

/**
 * Decode type Uint16 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_uint16_decode(
    struct uper_programming_types_uint16_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Uint32 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_uint32_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_uint32_t *src_p);

/**
 * Decode type Uint32 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_uint32_decode(
    struct uper_programming_types_uint32_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Uint64 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_uint64_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_uint64_t *src_p);

/**
 * Decode type Uint64 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_uint64_decode(
    struct uper_programming_types_uint64_t *dst_p,
    const uint8_t *src_p,
    size_t size);

/**
 * Encode type Uint8 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Buffer to encode into.
 * @param[in] size Size of dst_p.
 * @param[in] src_p Data to encode.
 *
 * @return Encoded data length or negative error code.
 */
ssize_t uper_programming_types_uint8_encode(
    uint8_t *dst_p,
    size_t size,
    const struct uper_programming_types_uint8_t *src_p);

/**
 * Decode type Uint8 defined in module ProgrammingTypes.
 *
 * @param[out] dst_p Decoded data.
 * @param[in] src_p Data to decode.
 * @param[in] size Size of src_p.
 *
 * @return Number of bytes decoded or negative error code.
 */
ssize_t uper_programming_types_uint8_decode(
    struct uper_programming_types_uint8_t *dst_p,
    const uint8_t *src_p,
    size_t size);

#endif